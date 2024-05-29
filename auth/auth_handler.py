import time
from typing import Dict, List
import jwt
from decouple import config
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, Request

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")
REFRESH_TOKEN_SECRET = config("refresh_token_secret", default="refresh_token_secret.token_hex(10)")
REFRESH_TOKEN_ALGORITHM = config("refresh_token_algorithm")

def token_response(access_token: str, refresh_token: str) -> Dict[str, str]:
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

def signJWT(email: str,id:str, roles: List[str]) -> Dict[str, str]:
    access_token_payload = {
        "email": email,
        "id": id,
        "roles": roles,
        "expires": time.time() + 60 * 60 * 24  # 24 hours
    }
    access_token = jwt.encode(access_token_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    refresh_token_payload = {
        "email": email,
        "id": id,
        "roles": roles,
        "expires": time.time() + 60 * 60 * 24 * 7  # 1 week
    }
    refresh_token = jwt.encode(refresh_token_payload, REFRESH_TOKEN_SECRET, algorithm=REFRESH_TOKEN_ALGORITHM)

    return token_response(access_token, refresh_token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded_token["expires"] >= time.time():
            return decoded_token
        return None
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def refresh_access_token(refresh_token: str) -> Dict[str, str]:
    try:
        decoded_token = jwt.decode(refresh_token, REFRESH_TOKEN_SECRET, algorithms=[REFRESH_TOKEN_ALGORITHM])
        email = decoded_token["email"]
        id=decoded_token["id"]
        roles = decoded_token["roles"]

        if decoded_token["expires"] < time.time():
            raise HTTPException(status_code=401, detail="Refresh token has expired")

        access_token_payload = {
            "email": email,
            "id":id,
            "roles": roles,
            "expires": time.time() + 60 * 60 * 24  # 24 hours
        }
        access_token = jwt.encode(access_token_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return token_response(access_token, refresh_token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        try:
            payload = decodeJWT(jwtoken)
            return payload is not None
        except:
            return False

    def get_current_user(self, token: str = Depends(HTTPBearer())):
        try:
            payload = decodeJWT(token.credentials)
            if payload is None:
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return payload
        except:
            raise HTTPException(status_code=403, detail="Invalid token or expired token.")

    def has_role(self, roles: List[int]):
        def role_checker(user: dict = Depends(self.get_current_user)):
            user_roles = user.get("roles", [])
            if isinstance(user_roles, int):
                user_roles = [user_roles]
            else:
                user_roles = [int(role) for role in user_roles]
            if any(role in user_roles for role in roles):
                return user
            raise HTTPException(status_code=403, detail="Operation not permitted")

        return role_checker


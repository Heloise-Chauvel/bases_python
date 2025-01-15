from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from google.oauth2 import id_token
from google.auth.transport import requests
from fastapi import HTTPException, Security

#init schéma Bearer
security_http_bearer = HTTPBearer()

GOOGLE_ISSUER = "https://accounts.google.com"

def verify_google_jwt(token: str):
    try:
        #valide le token avec la clé pubique Google
        id_info = id_token.verify_oauth2_token(token, requests.Request())

        if id_info['iss'] != GOOGLE_ISSUER:
            raise ValueError("Token issuer is invalid")

        return id_info
    except ValueError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token {e}")

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security_http_bearer)):
    token = credentials.credentials
    return verify_google_jwt(token)

def get_current_user_admin(credentials: HTTPAuthorizationCredentials = Security(security_http_bearer)):
    id_info = get_current_user(credentials)
    if id_info['email'] != 'chauvel.h@gmail.com':
        raise HTTPException(status_code=403, detail=f"Invalid role")
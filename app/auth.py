from passlib.context import CryptContext
from fastapi import HTTPException
from jwt import encode, decode, ExpiredSignatureError, InvalidTokenError
from passlib.context import CryptContext
import datetime

from app import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password_hash(plain_password: str):
    return pwd_context.hash(plain_password)


def verify_password(plain_password:str, hash_password: str):
    return pwd_context.verify(plain_password, hash_password)

def encode_token(sub: dict):
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        minutes=settings.Settings().ACESS_TOKEN_EXPIRE
    )
    payload = {"exp": expire,
               "sub": sub
               }
    encoded = encode(
        payload,
        settings.Settings().SECRET_KEY,
        'HS256'
    )
    return f"Bearer {encoded}"


def decode_token(Autentication: str, key):
    try:
        if not "Bearer" in Autentication:
            raise HTTPException(
                status_code=401,
                detail="Desculpe Você nao tem Permissão, Chave de acesso Invalida",
            )
        token = Autentication.split(sep=' ')[1].replace('\"', "")
        payload = decode(token, settings.Settings().SECRET_KEY, algorithms='HS256')
        if "user_id" in payload["sub"]: 
            if key == payload["sub"]["profile"]:
                return payload["sub"]
            else:
                raise HTTPException(status_code=402, detail="nivel de permissão invalido")
        
        
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail=[
                {"msg": "Desculpe Você nao tem Permissão, Chave de acesso expirada!"}
            ],
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail=[
                {"msg": "token invalido, Chave de acesso Invalida!"}
            ],
        )
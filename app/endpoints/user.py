from fastapi import APIRouter, Header
from typing import List, Annotated

from app import schemas, models, auth

router = APIRouter(tags=["User"])


@router.get("/user/", status_code=200)
def get_user():
    return models.User.get_all()


@router.post("/user/")
def post_user(json_data: schemas.PostUser):
    data = models.User(**json_data.model_dump())
    return data.create()

@router.put("/user/")
def put_user(json_data: schemas.PutUser, Autentication: Annotated[str, Header()]):
    payload =  auth.decode_token(Autentication, "manage collect point")

    models.User.update(payload['user_id'], **json_data.model_dump(exclude_unset=True))
    
    return "usuario atualizado com sucesso"

@router.delete("/user/{username}")
def delete_user(username, Autentication: Annotated[str, Header()]):
    payload =  auth.decode_token(Autentication, "manage collect point")

    models.User.delete(username)
    
    return "usuario deletado com sucesso"

from fastapi import APIRouter, HTTPException
from app import auth

from app import schemas, models, settings

router = APIRouter(tags=["login"])


@router.post("/login-maneger/", status_code=200)
def login(data: schemas.PostLogin):
    try:
        user = models.User.login(**data.model_dump(exclude_unset=True))

        sub = {'user_id':str(user.id), 'profile': "manage collect point"}
        return auth.encode_token(sub)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

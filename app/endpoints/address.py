from fastapi import APIRouter, HTTPException
from app import auth

from app import schemas, models, settings

router = APIRouter(tags=["address"])

@router.get("/address/", status_code=200)
def get_address():
    return models.Address.get_all()


@router.post("/address/")
def post_address(json_data: schemas.PostAddress):
    data = models.Address(**json_data.model_dump())
    return data.create()

@router.put("/address/{id}")
def put_address(id, json_data: schemas.PutAddress, ):
    return models.Address.update(id, **json_data.model_dump(exclude_unset=True))
    
     

@router.delete("/address/{id}")
def delete_address(id):
    models.Address.remove(id)
    return "endereco deletado com sucesso"

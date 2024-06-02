from fastapi import APIRouter, HTTPException
from app import auth

from app import schemas, models, settings

router = APIRouter(tags=["collect_point"])

@router.get("/collect_point/", status_code=200)
def get_collect_point():
    return models.CollectPoint.get_all()


@router.post("/collect_point/")
def post_collect_point(json_data: schemas.PostCollectPoint):
    data = models.CollectPoint(**json_data.model_dump())
    return data.create()

@router.put("/collect_point/{id}")
def put_collect_point(id, json_data: schemas.PutCollectPoint, ):
    return models.CollectPoint.update(id, **json_data.model_dump(exclude_unset=True))
    
     

@router.delete("/collect_point/{id}")
def delete_collect_point(id):

    models.CollectPoint.remove(id)
    return "ponto de coleta deletado com sucesso"

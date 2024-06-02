from fastapi import APIRouter, HTTPException
from app import auth

from app import schemas, models, settings

router = APIRouter(tags=["donation_to_receive"])

@router.get("/donation_to_receive/", status_code=200)
def get_donation_to_receive():
    return models.DonationsToReceive.get_all()


@router.post("/donation_to_receive/")
def post_donation_to_receive(json_data: schemas.PostDonationToReceive):
    data = models.DonationsToReceive(**json_data.model_dump())
    return data.create()

@router.put("/donation_to_receive/{id}")
def put_donation_to_receive(id, json_data: schemas.PutDonationToReceive, ):
    return models.DonationsToReceive.update(id, **json_data.model_dump(exclude_unset=True))
    

@router.delete("/donation_to_receive/{id}")
def delete_donation_to_receive(id):

    models.DonationsToReceive.remove(id)
    return "recebimento de doacoes deletado com sucesso"
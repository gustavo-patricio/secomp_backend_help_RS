from sqlalchemy import select, Date, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import relationship

from typing import List
from fastapi import HTTPException


from app import auth, session, base_model

class User(base_model.Base):
    username: Mapped[str] = mapped_column(String, unique=True)
    email : Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)

    @classmethod
    def login(cls, username: str, password: str):

        _db = session.Session()
        result = _db.execute(select(cls).where(cls.username == username))
        user = result.scalars().one()
        if not user:
            raise HTTPException(status_code=404, detail="Usuario não encontrado")
        if not auth.verify_password(password, user.password):
            raise HTTPException(status_code=403, detail="senha invalida")
        return user

    @classmethod
    def delete(cls, username:str):
        try:
            _db = session.Session()
            stmt = select(cls).where(cls.username == username)
            data = _db.execute(stmt).scalar_one()
            if not data:
                raise HTTPException(
                    status_code=404, detail="usuario não encontrado"
                )
            _db.delete(data)
            _db.commit()
        except Exception as e:
            _db.rollback()
            raise e

        finally:
            _db.close()
        
class CollectPoint(base_model.Base):
    """Ponto de coleta

    Atributed:
        name_point (str): nome do ponto
        start_time (str): horario inicial de funcionamento
        end_time (str): horario final de funcionamento
        receiving_donations (bool): aceitando doações
    """
    name_point: Mapped[str] = mapped_column(String) 
    start_time: Mapped[str] = mapped_column(String)
    end_time: Mapped[str] = mapped_column(String)   
    receiving_donations: Mapped[bool] = mapped_column(Boolean)

    donetions_point: Mapped[List["DonationsToReceive"]] = relationship(back_populates="collect_point", cascade="all, delete-orphan")
    address: Mapped["Address"] = relationship(back_populates="collect_point", cascade="all, delete-orphan")

class DonationsToReceive(base_model.Base):
    """Tipo de Doacao que se pode receber

    Atributes:
        description (str): descricao contendo horientacoes para a doacao
        items_type (str): tipos de itens
        collection_point_id (int): chave estrangeira
    """

    description: Mapped[str] = mapped_column(Text)
    items_type: Mapped[str] = mapped_column(String)
    collection_point_id: Mapped[int] = mapped_column(ForeignKey("collectpoint.id"))
    
    collect_point: Mapped["CollectPoint"] = relationship(back_populates="donetions_point")

class Address(base_model.Base):
    """endereço

    Atributos:
        street (str): rua
        number (str): numero
        district (str): bairro
        complement (str): complemento
    """
    street: Mapped[str] = mapped_column(String)
    number: Mapped[str] = mapped_column(String)
    district: Mapped[str] = mapped_column(String)
    complement: Mapped[str]
    collection_point_id: Mapped[int] = mapped_column(ForeignKey("collectpoint.id"))

    collect_point: Mapped["CollectPoint"] = relationship(back_populates="address")

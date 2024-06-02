from sqlalchemy import select, Date, String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, DeclarativeBase

from fastapi import HTTPException

from .session import Session


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)

    def create(cls):
        try:
            _db = Session()
            data = cls
            _db.add(data)
            _db.commit()
            _db.refresh(data)
        finally:
            _db.close()
        return data

    @classmethod
    def get(cls, id):
        try:
            _db = Session()
            query = select(cls).where(cls.id==id)
            data = _db.scalars(query).first()
            if not data:
                raise HTTPException(
                    status_code=404, detail = "dado não encontrado"
                )
        except Exception as e:
            raise e
        finally:
            _db.close()
        return data

    @classmethod
    def get_all(cls):
        try:
            _db = Session()
            query = select(cls)
            data = _db.scalars(query).all()
        finally:
            _db.close()

        return data

    @classmethod
    def get_page(cls, limit:int=None, offset:int=None, key:str=None, value:str=None,  all: bool = None):
        try:
            _db = Session()
            query_obj = _db.query(cls)
            if all:
                data = query_obj.all()
            elif key and value:
                data = query_obj.filter(getattr(cls, key)==value).limit(limit).offset(offset).all()   
            elif limit and offset:
                data = query_obj.limit(limit).offset(offset).all()
            else:
                raise
        except:
            _db.rollback()
            raise HTTPException(status_code=404, detail=[{'msg':'erro interno'}])
        finally:
            _db.close()
            
        return data

        

    @classmethod
    def remove(cls, request_id):
        try:
            _db = Session()
            stmt = select(cls).where(cls.id == request_id)
            data = _db.execute(stmt).scalar_one()
            if not data:
                raise HTTPException(
                    status_code=404, detail="dado não encontrado"
                )
            _db.delete(data)
            _db.commit()
        except Exception as e:
            _db.rollback()
            raise e

        finally:
            _db.close()

        return "usuario deletado"

    @classmethod
    def update(cls, request_id, **request_data):
        try:
            _db = Session()
            stmt = select(cls).where(cls.id == request_id)
            data = _db.execute(stmt).scalar_one()
            if not data:
                raise HTTPException(
                    status_code=404, detail=[{"msg": "Dado não encontrado"}]
                )
            for key, value in request_data.items():
                setattr(data, key, value)

            _db.add(data)
            _db.commit()
            _db.refresh(data)

            return data
        except Exception as e:
            _db.rollback()
            raise e
        
        finally:
            _db.close()

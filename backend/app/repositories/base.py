from typing import Any, Generic, Type, TypeVar
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: Any):
        return db.get(self.model, id)

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def create(self, db: Session, obj: ModelType):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, obj: ModelType):
        db.delete(obj)
        db.commit()

    def update(
        self,
        db: Session,
        obj: ModelType,
        data: dict,
    ):
        for campo, valor in data.items():
            setattr(obj, campo, valor)

        db.commit()
        db.refresh(obj)

        return obj 
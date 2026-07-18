from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.base import BaseRepository
from app.models.enums import UserRole

class UserRepository(BaseRepository[User]):

    def __init__(self):
        super().__init__(User)

    def get_by_email(self, db: Session, email: str):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_by_id(self, db: Session, user_id):
        return self.get(db, user_id)
    
    def get_all_gestores(self, db: Session):
        return (
            db.query(User)
            .filter(User.perfil == UserRole.GESTOR)
            .all()
        )


    def get_gestor(self, db: Session, gestor_id):
        return (
            db.query(User)
            .filter(
                User.id == gestor_id,
                User.perfil == UserRole.GESTOR,
            )
            .first()
        )

user_repository = UserRepository()
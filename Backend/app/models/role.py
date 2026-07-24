from sqlalchemy import Column, String
from app.database.base import BaseModel


class RoleModel(BaseModel):
    __tablename__ = "roles"

    name = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(String(255), nullable=True)

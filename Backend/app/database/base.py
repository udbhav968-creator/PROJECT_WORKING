import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base, declared_attr


class CustomBase:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"


Base = declarative_base(cls=CustomBase)


class BaseModel(Base):
    """
    Industry-Level Base Model:
    - Primary Key: UUIDv4 string (prevents sequential ID enumeration attacks)
    - Timestamps: created_at, updated_at
    - Soft Delete: is_deleted boolean flag for regulatory compliance (medical records)
    """
    __abstract__ = True

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    is_deleted = Column(Boolean, default=False, nullable=False, index=True)

    def soft_delete(self):
        """Soft deletes the instance by setting is_deleted=True."""
        self.is_deleted = True

    def restore(self):
        """Restores a soft-deleted instance."""
        self.is_deleted = False

    def to_dict(self):
        """Helper to convert model attributes to dictionary."""
        return {
            c.name: getattr(self, c.name).isoformat() if isinstance(getattr(self, c.name), datetime) else getattr(self, c.name)
            for c in self.__table__.columns
        }

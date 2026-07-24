from sqlalchemy import Column, String, DateTime
from app.database.base import BaseModel


class AppointmentModel(BaseModel):
    __tablename__ = "appointments"

    patient_name = Column(String(255), nullable=False)
    patient_phone = Column(String(50), nullable=False)
    patient_email = Column(String(255), nullable=True)
    doctor_name = Column(String(255), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    status = Column(String(50), default="scheduled", nullable=False, index=True)
    notes = Column(String(500), nullable=True)

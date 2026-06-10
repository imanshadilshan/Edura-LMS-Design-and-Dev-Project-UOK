
import uuid

from sqlalchemy import Column, Integer, String, UUID, DateTime, Boolean, func, Float
from app.db import Base

class ClassPaymentPrice(Base):
    __tablename__ = "class_payment_price"
    class_payment_price_id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(UUID(as_uuid=True), nullable=False)
    class_price = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Payment(Base):
    __tablename__ = "payment"

    payment_id = Column(UUID(as_uuid=True), primary_key=True, autoincrement=True)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    class_id = Column(UUID(as_uuid=True), nullable=False)
    date = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
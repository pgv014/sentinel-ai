from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from .database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    type = Column(String)
    status = Column(String, default="Healthy")
    last_seen = Column(DateTime, default=datetime.utcnow)


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)

    device_name = Column(String, index=True)

    temperature = Column(Float)

    vibration = Column(Float)

    pressure = Column(Float)

    power = Column(Float)

    timestamp = Column(DateTime, default=datetime.utcnow)

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String)
    severity = Column(String)
    risk = Column(Float)
    confidence = Column(Float)
    message = Column(String)
    recommendation = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
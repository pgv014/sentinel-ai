from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Telemetry
from ..services.analysis import calculate_risk

router = APIRouter()


@router.post("/telemetry")
def add_telemetry(data: dict, db: Session = Depends(get_db)):
    try:
        reading = Telemetry(
            device_name=data["device_name"],
            temperature=data["temperature"],
            vibration=data["vibration"],
            pressure=data["pressure"],
            power=data["power"],
        )

        db.add(reading)
        db.commit()
        db.refresh(reading)

        return {"status": "saved"}

    except Exception as e:
        db.rollback()
        return {"error": str(e)}


@router.get("/telemetry")
def get_telemetry(db: Session = Depends(get_db)):
    readings = db.query(Telemetry).order_by(Telemetry.id.desc()).limit(50).all()
    return readings

    db.add(reading)
    db.commit()

    return {"status": "saved"}


@router.get("/telemetry")
def get_telemetry(db: Session = Depends(get_db)):
    readings = db.query(Telemetry).order_by(Telemetry.id.desc()).limit(50).all()

    return readings

@router.get("/analysis")
def analysis(db: Session = Depends(get_db)):
    return calculate_risk(db)
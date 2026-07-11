from sqlalchemy.orm import Session
from sqlalchemy import desc

from ..models import Telemetry


def calculate_risk(db: Session):
    devices = db.query(Telemetry.device_name).distinct().all()

    results = []

    for d in devices:
        device = d[0]

        readings = (
            db.query(Telemetry)
            .filter(Telemetry.device_name == device)
            .order_by(desc(Telemetry.timestamp))
            .limit(10)
            .all()
        )

        if not readings:
            continue

        avg_temp = sum(r.temperature for r in readings) / len(readings)
        avg_vibration = sum(r.vibration for r in readings) / len(readings)
        avg_pressure = sum(r.pressure for r in readings) / len(readings)
        avg_power = sum(r.power for r in readings) / len(readings)

        # Trend
        trend = 0
        if len(readings) >= 2:
            trend += readings[0].temperature - readings[-1].temperature
            trend += (readings[0].vibration - readings[-1].vibration) * 20

        risk = 0

        if avg_temp > 60:
            risk += 35
        elif avg_temp > 50:
            risk += 20

        if avg_vibration > 0.6:
            risk += 35
        elif avg_vibration > 0.4:
            risk += 20

        if avg_power > 125:
            risk += 20

        if avg_pressure < 90:
            risk += 10

        risk += max(0, int(trend))
        risk = min(risk, 100)

        if risk >= 80:
            severity = "Critical"
            recommendation = "Inspect immediately."
        elif risk >= 60:
            severity = "High"
            recommendation = "Schedule maintenance."
        elif risk >= 40:
            severity = "Medium"
            recommendation = "Monitor closely."
        else:
            severity = "Healthy"
            recommendation = "No action required."

        results.append({
            "device": device,
            "risk": risk,
            "severity": severity,
            "temperature": round(avg_temp, 2),
            "vibration": round(avg_vibration, 2),
            "pressure": round(avg_pressure, 2),
            "power": round(avg_power, 2),
            "recommendation": recommendation
        })

    return sorted(results, key=lambda x: x["risk"], reverse=True)
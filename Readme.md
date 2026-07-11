# Sentinel AI

## Overview
A predictive maintenance dashboard for industrial equipment.

## Features
- Live telemetry ingestion
- SQLite storage
- Risk scoring
- Severity classification
- Recommendations
- Live dashboard

## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- React
- Axios

## Architecture
Simulator → FastAPI → SQLite → Analysis Engine → React Dashboard

## Assumptions
- Simulated devices
- Four metrics per device
- Risk computed from thresholds and recent trends

## Future Improvements
- WebSockets
- ML-based anomaly detection
- Kafka
- PostgreSQL
- Time-series database
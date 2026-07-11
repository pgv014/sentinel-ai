# 🛰️ Sentinel AI – Predictive Maintenance Dashboard

Sentinel AI is a full-stack predictive maintenance platform that monitors industrial equipment using simulated IoT telemetry and analyzes device health in real time.

The system collects telemetry data, calculates a risk score based on equipment behavior, and displays actionable insights through a live dashboard.

---

## 🚀 Features

- 📊 Real-time equipment monitoring
- ⚡ Predictive risk analysis
- 🌡️ Telemetry tracking (Temperature, Vibration, Pressure, Power)
- 🚨 Automatic health classification
- 📈 Live React dashboard
- 🔗 REST APIs with FastAPI
- 📄 Interactive API documentation (Swagger UI)

---

## 🏗️ Tech Stack

### Frontend
- React
- Axios
- CSS

### Backend
- FastAPI
- SQLAlchemy
- SQLite

### Database
- SQLite

---

## 📂 Project Structure

```
sentinel-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── models.py
│   │   ├── database.py
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/pgv014/sentinel-ai.git
cd sentinel-ai
```

---

### 2. Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate      # macOS/Linux

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger Docs

```
http://127.0.0.1:8000/docs
```

---

### 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Health Check |
| POST | `/telemetry` | Add telemetry reading |
| GET | `/telemetry` | Fetch telemetry |
| GET | `/analysis` | Predictive maintenance analysis |

---

## 🧠 Risk Analysis

The backend analyzes the latest telemetry readings for every device.

The following metrics are evaluated:

- Temperature
- Vibration
- Pressure
- Power Consumption

Each metric contributes to an overall risk score.

Risk Levels:

| Risk | Status |
|------|--------|
| 0–39 | Healthy |
| 40–59 | Medium |
| 60–79 | High |
| 80–100 | Critical |

---

## 📷 Dashboard

The dashboard displays:

- Healthy Devices
- Warning Devices
- Critical Devices
- Device Risk Scores
- Sensor Readings
- Maintenance Recommendations

---

## 🔮 Future Improvements

- Machine Learning based anomaly detection
- MQTT / Kafka integration
- Authentication
- PostgreSQL support
- Docker deployment
- Email / SMS alerts
- Historical analytics

---

## 👨‍💻 Author

**Parth Gupta**

GitHub:
https://github.com/pgv014

---

## 📄 License

This project is developed for educational and demonstration purposes.

# 🚗 AutoNexus — AI-Powered Predictive Vehicle Maintenance Backend

A production-grade FastAPI backend that ingests real OBD-II sensor data from 81+ vehicles and runs a multi-agent AI system to predict component failures before they happen.

> **My role:** Backend lead & integration owner — FastAPI server, database design, master agent orchestrator, and integration of ML models, frontend, and notification agents built by teammates.

---

## What It Does

- Predicts vehicle failures **7–90 days in advance** using an XGBoost model (94% accuracy)
- Coordinates **8 specialized AI agents** — diagnosis, engagement, scheduling, feedback, manufacturing insights, UEBA security, and more
- Sends **time-aware alerts** via Twilio voice calls, SMS, and email (no midnight calls — 9 AM–8 PM only)
- Generates **RCA/CAPA PDF reports** for fleet-wide failure pattern analysis
- Monitors for anomalous behavior via **UEBA (Isolation Forest)** security agent

---

## Tech Stack

- **Framework:** FastAPI 0.100+
- **Database:** SQLite (dev)  
- **ML:** XGBoost, Scikit-learn, SHAP
- **Agents:** LangChain / LangGraph orchestration
- **Notifications:** Twilio Voice + SMS, SendGrid email
- **Auth & Security:** Role-based access control, UEBA anomaly detection
- **Docs:** Auto-generated Swagger UI at `/docs`

---

## Quickstart

### 1. Clone & install

```bash
git clone https://github.com/Rashmivid/Autonexus-backend.git
cd Autonexus-backend
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
DATABASE_URL=sqlite:///./autonexus.db      
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_PHONE_NUMBER=+1xxxxxxxxxx
SENDGRID_API_KEY=your_key
```

> SQLite works out of the box with no extra setup — recommended for local development.

### 3. Seed the database

```bash
curl -X POST http://localhost:8000/admin/seed
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

Visit **http://localhost:8000/docs** for the full interactive API.

---

## Key Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/vehicles` | List all vehicles with health status |
| `GET` | `/vehicles/{id}` | Vehicle details + sensor readings |
| `POST` | `/vehicles/{id}/analyze` | Run full AI agent analysis |
| `POST` | `/vehicles/{id}/notify` | Trigger time-aware Twilio alert |
| `POST` | `/vehicles/{id}/book` | Schedule a service appointment |
| `GET` | `/vehicles/{id}/feedback` | Retrieve feedback survey |
| `GET` | `/manufacturing/insights` | Fleet-wide RCA/CAPA report |
| `GET` | `/security/ueba` | UEBA anomaly detection status |
| `POST` | `/admin/seed` | Seed database with OBD-II data |
| `POST` | `/admin/randomize` | Randomize sensor readings for demo |

Full docs at `/docs` (Swagger) or `/redoc` (ReDoc).

---

## Agent Architecture

```
MasterAgent (Orchestrator)
├── DataAnalysisAgent     — Sensor threshold analysis, anomaly detection
├── DiagnosisAgent        — XGBoost failure prediction (94% accuracy)
├── EngagementAgent       — Time-aware voice/SMS/email notifications
├── SchedulingAgent       — Urgency-based appointment booking
├── FeedbackAgent         — 15-question post-service survey
├── ManufacturingInsightsAgent — Fleet RCA/CAPA PDF reports
└── UEBAAgent             — Isolation Forest security monitoring
```

---

## Dataset

Real OBD-II sensor data — **DOI: 10.35097/1130**
- 81 vehicles, 1,200+ samples
- 6 sensor features: brake temp, oil pressure, engine temp, tire pressure, brake fluid, mileage
- Hosted on Hugging Face: `divyanshi-02/autonexus-p2-ml-models`

---

## Project Structure

```
Autonexus-backend/
├── main.py                  # FastAPI app, startup, routing
├── models.py                # SQLAlchemy ORM models
├── agents/
│   ├── master_agent.py      # Orchestrator
│   ├── diagnosis_agent.py   # ML prediction
│   ├── engagement_agent.py  # Notifications
│   ├── scheduling_agent.py  # Booking
│   ├── feedback_agent.py    # Survey
│   ├── manufacturing_agent.py
│   └── ueba_agent.py        # Security
├── routers/
│   ├── vehicles.py
│   ├── admin.py
│   └── manufacturing.py
├── load_vehicles_from_OBD.py  # Data seeding
├── requirements.txt
└── .env.example
```

---

## Part of a Larger System

This repo is the backend. The full AutoNexus system also includes:
- **Frontend:** React/Vite dashboard (separate repo)
- **ML models:** Hosted on Hugging Face

---

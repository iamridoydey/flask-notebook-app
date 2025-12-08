# 🛠️ Backend – Flask Notebook API

This is the **backend** service for the Notebook App.  
It is built with **Flask (Python)**, uses **SQLAlchemy + PyMySQL** for database access, and exposes a REST API for the React frontend.

---

## 🚀 Features
- Auto‑creates the MySQL database if missing
- Initializes a `notes` table with `id`, `note`, and `completed` fields
- REST API endpoints for full CRUD:
  - `GET /notes` → fetch all notes
  - `POST /notes` → add a new note
  - `PUT /notes/<id>` → toggle completion status
  - `DELETE /notes/<id>` → delete a note
- CORS enabled for frontend requests. Example: `http://localhost:3000`
- Health check endpoint (`/health`)

---

## ⚙️ Setup Instructions

### 1. Local Installation
Create and activate a virtual environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the application
```bash
python app.py
```

## 2. Docker Setup
Build docker image
```bash
docker build -t notebook-api .
```
Run the docker image
```bash
docker run -it --name <container-name> -p <host-port>:5000 -e CORS_ORIGINS=<frontend-url:port / url> notebook-api
```

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
- CORS enabled for frontend requests from `http://localhost:5173`
- Health check endpoint (`/health`)

---

## ⚙️ Setup Instructions

### 1. Install dependencies
Create and activate a virtual environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

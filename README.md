# 📓 Flask + React Notebook App

A simple two‑tier web application built with **Flask (Python)** for the backend and **React (TypeScript + Tailwind)** for the frontend.  
It allows users to create, toggle (mark completed), and delete notes, with persistence in a MySQL database.

---

## 🚀 Features
- **Backend (Flask + SQLAlchemy + PyMySQL)**
  - Auto‑creates the database if missing
  - Initializes a `notes` table with `id`, `note`, and `completed` fields
  - REST API endpoints:
    - `GET /notes` → fetch all notes
    - `POST /notes` → add a new note
    - `PUT /notes/<id>` → toggle completion status
    - `DELETE /notes/<id>` → delete a note
  - CORS enabled for React frontend

- **Frontend (React + Vite + Tailwind)**
  - Displays notes in a clean card list
  - Add new notes via input
  - Toggle completion with a checkbox
  - Delete notes with a remove button
  - Responsive layout using TailwindCSS

---

## 🛠 Tech Stack
- **Backend:** Flask, SQLAlchemy, PyMySQL, Flask‑CORS
- **Frontend:** React, TypeScript, Vite, TailwindCSS
- **Database:** MySQL

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/flask-notebook-app.git
cd flask-notebook-app
```

## 🐳 Running the Application with Docker & Docker Compose

This repository is fully containerized. All services (backend, frontend, and database) are defined in `docker-compose.yml`.

### Start the application
```bash
docker compose up --build
```

### 🐳 Remove the container

```bash
docker compose down
```

# 🖥️ Frontend – React + TypeScript + Vite

This is the **frontend** for the Flask Notebook App.  
It is built with **React (TypeScript)**, powered by **Vite** for fast development, and styled with **TailwindCSS**.

---

## 🚀 Features
- Built with **React + TypeScript** for type safety and modern UI patterns
- Uses **Vite** for lightning‑fast dev server and HMR (Hot Module Replacement)
- **TailwindCSS** for responsive, utility‑first styling
- Connects to Flask backend via REST API (`/notes`)
- Implements full CRUD:
  - Add new notes
  - Toggle completion (checkbox)
  - Delete notes
  - Fetch notes on reload

---

## ⚙️ Setup Instructions

### 1. Local Setup
```bash
cd frontend
npm install
```

## 2. Docker Setup
Build docker image
```bash
docker build -t notebook-api .
```
### Run the docker image
- Change your working director to /flask-notebook-app/frontend/public/
- Change the **VITE_API_URL** as per your backend-api
- Then run the container with following commands
```bash
docker run -it --name <container-name> -p 3000:3000 \
  -v $(pwd)/config.js:/app/dist/config.js \
  notebook-ui
```

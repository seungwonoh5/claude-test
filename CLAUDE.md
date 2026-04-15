# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture

Monorepo with two independently deployed services:

- `frontend/` — React 18 + Vite. Fetches `/api/hello` from the backend and renders the response. Deployed to **Vercel**.
- `backend/` — Python FastAPI. Exposes `GET /api/hello`. Deployed to **Railway**.

The frontend reads `VITE_API_URL` at build time (via `import.meta.env`) to point at the backend. The backend reads `ALLOWED_ORIGINS` (comma-separated) to configure CORS.

## Local development

**Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# Runs on http://localhost:8000
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
# Runs on http://localhost:5173
# Set VITE_API_URL=http://localhost:8000 in frontend/.env.local
```

## Deployment

### Railway (backend)
- Connect the repo and set **Root Directory** to `backend/`
- Railway uses `Procfile` to start the server
- Set env var: `ALLOWED_ORIGINS=https://your-app.vercel.app`

### Vercel (frontend)
- Connect the repo and set **Root Directory** to `frontend/`
- Vercel auto-detects Vite — no extra config needed
- Set env var: `VITE_API_URL=https://your-app.up.railway.app`

Start the FastAPI backend development server.

```bash
cd backend && pip install -r requirements.txt && uvicorn main:app --reload
```

Run the command above. The server will be available at http://localhost:8000. Remind the user to set `ALLOWED_ORIGINS` in `backend/.env` if they haven't already.

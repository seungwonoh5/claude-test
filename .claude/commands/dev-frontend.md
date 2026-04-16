Start the React/Vite frontend development server.

```bash
cd frontend && [ ! -d node_modules ] && npm install; npm run dev
```

Run the command above. The app will be available at http://localhost:5173. Remind the user to create `frontend/.env.local` with `VITE_API_URL=http://localhost:8000` if they haven't already.

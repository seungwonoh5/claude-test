import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

app = FastAPI()

allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))


@app.get("/api/hello")
def hello():
    return {"message": "Hello, World!"}


@app.get("/api/users")
def get_users():
    response = supabase.table("users").select("*").limit(2).execute()
    return {"users": response.data}

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime
import uvicorn

app = FastAPI(title="LMS UTS Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

users_db = []
courses_db = []

@app.get("/")
def root():
    return {
        "message": "LMS Backend UTS OK!",
        "students": len(users_db),
        "courses": len(courses_db)
    }

@app.get("/api/v1/users")
def get_users() -> List[dict]:
    return users_db

@app.post("/api/v1/users")
def create_user(full_name: str, email: str):
    user = {
        "id": len(users_db) + 1,
        "full_name": full_name,
        "email": email,
        "created_at": str(datetime.now())
    }
    users_db.append(user)
    return {"status": "success", "user": user}

@app.get("/api/v1/courses")
def get_courses() -> List[dict]:
    return courses_db

@app.post("/api/v1/courses")
def create_course(title: str, price: float = 0.0):
    course = {
        "id": len(courses_db) + 1,
        "title": title,
        "price": price
    }
    courses_db.append(course)
    return {"status": "success", "course": course}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
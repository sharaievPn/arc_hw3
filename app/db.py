from fastapi import FastAPI, Body, HTTPException

db_service = FastAPI()

people_db = [
    {"name": "Sarah", "age": 27, "description": "Software engineer who loves hiking and painting."},
    {"name": "James", "age": 34, "description": "Data analyst with a passion for chess and AI."},
    {"name": "Emma", "age": 22, "description": "College student majoring in economics, enjoys photography."}
]

@db_service.get("/")
def info():
    return {"info": "Database service: stores user information; give ability to retrieve user data and add new users to db; not available for external users"}

@db_service.get("/health")
def health():
    return {"status": "ok"}

@db_service.get("/users")
def users():
    return people_db

@db_service.post("/new_user", status_code=201)
def add_user(user: dict = Body(...)):
    if "name" not in user or "age" not in user or "description" not in user:
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    people_db.append({"name": user['name'], "age": user["age"], "description": user["description"]})

    return {"status": "ok", "message": f"Successfully add new user: {user}"}

from fastapi import FastAPI, Body, HTTPException, Depends, Request
from requests import get, post
from dotenv import load_dotenv
from os import getenv

load_dotenv()

client = FastAPI()

APP_TOKEN = getenv("APP_TOKEN")
DB_CONNECTION_URL = getenv("DB_CONNECTION_URL")
BUSINESS_CONNECTION_URL = getenv("BUSINESS_CONNECTION_URL")

def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

@client.get("/")
def info():
    return {"info": "Client service: give user ability to retrieve data of all users, add new user and get friendship suggestions based on user information"}

@client.get("/health")
def health():
    return {"status": "ok"}

@client.get("/users", dependencies=[Depends(verify_token)])
def user():
    health = get(f"{DB_CONNECTION_URL}/health").json()

    if health["status"] != "ok":
        raise HTTPException(status_code=503, detail="Service error")
    
    return get(f"{DB_CONNECTION_URL}/users").json()

@client.post("/new_user", dependencies=[Depends(verify_token)])
def new_user(user: dict = Body(...)):
    health = get(f"{DB_CONNECTION_URL}/health").json()

    if health["status"] != "ok":
        raise HTTPException(status_code=503, detail="Service error")

    return post(f"{DB_CONNECTION_URL}/new_user", json={"name": user['name'], "age": user['age'], "description": user['description']}).json()

@client.get("/friend", dependencies=[Depends(verify_token)])
def friend(name: str,
           age: str,
           description: str):
    
    health = get(f"{BUSINESS_CONNECTION_URL}/health").json()

    if health["status"] != "ok":
        raise HTTPException(status_code=503, detail="Service error")
    
    return get(f"{BUSINESS_CONNECTION_URL}/friend?name={name}&age={age}&description={description}").json()


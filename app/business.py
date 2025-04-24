from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from os import getenv
from requests import get, post

load_dotenv()

business_service = FastAPI()

BUSINESS_TOKEN = getenv("BUSINESS_TOKEN")
DB_CONNECTION_URL = getenv("DB_CONNECTION_URL")

def people_data():

    db_health = get(f"{DB_CONNECTION_URL}/health").json()

    if db_health['status'] != "ok":
        raise HTTPException(status_code=503, detail="Service error")
    
    return get(f"{DB_CONNECTION_URL}/users").json()

@business_service.get("/")
def info():
    return {"info": "Business service: returns suggestion, who can be a friend, for provided user data among available (in db) users"}

@business_service.get("/health")
def health():
    return {"status": "ok"}

@business_service.get("/friend")
def friends(name: str,
            age: str,
            description: str):
    
    users = people_data()

    response = post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {BUSINESS_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages":[
                {
                    "role": "system",
                    "content":
                    f"""
                    user list: {users}

                    Give a suggestion, who can be a friend for provided user data among available users in user list.
                    Returns response in such format:

                    The possible friend for you is:
                    name: user name from provided list
                    age: user age from provided list
                    info: user description from provided list
                    """
                },
                {
                    "role": "user", 
                    "content": f"Name: {name}, age: {age}, description: {description}"
                }
            ]
        })
    
    return response.json()["choices"][0]["message"]["content"]
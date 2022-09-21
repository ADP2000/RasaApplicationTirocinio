from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class CognitiveExercise(BaseModel):
    id: str
    name: str
    level: int

class CognitiveExercisesResult(BaseModel):
    id: str
    score: int

class Session(BaseModel):
    id: str
    exercises: list

class SessionResult(BaseModel):
    id: str
    exercises: list

session = Session(id = "1", exercises = [
    CognitiveExercise(id = "2", name = "esercizioA1", level = 2),
    CognitiveExercise(id = "3", name = "esercizioH1", level = 2),
])

@app.get("/session")
async def get_session():
    return session

@app.post("/session", status_code=201)
async def add_sessionResult(sessionResult: SessionResult):
    global session
    session = sessionResult
    return session

@app.post("/session", status_code=201)
async def add_sessionResult(session1: Session):
    global session
    session = session1
    return session
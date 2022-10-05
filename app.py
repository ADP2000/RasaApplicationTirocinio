# uvicorn app:app --reload ---> comando per far partire il server dell'API REST
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
    cognitiveExerciseResult: list

easySession = Session(id = "d290f1ee-6c54-4b01-90e6-d701748f0851", exercises = [
    CognitiveExercise(id = "bd5a4df8-3cc1-11ed-a261-0242ac120002", name = "esercizioA1", level = 1),
    CognitiveExercise(id = "c92350c6-3cc1-11ed-a261-0242ac120002", name = "esercizioH2", level = 2),
    CognitiveExercise(id = "d77ddc40-3cc1-11ed-a261-0242ac120002", name = "esercizioC1", level = 1)
])

hardSession = Session( id = "4c45382a-3cc2-11ed-a261-0242ac120002", exercises = [
    CognitiveExercise(id = "633d3afa-3cc2-11ed-a261-0242ac120002", name = "esercizioA3", level = 3),
    CognitiveExercise(id = "7d722c82-3cc2-11ed-a261-0242ac120002", name = "esercizioH1", level = 3),
    CognitiveExercise(id = "9177aa04-3cc2-11ed-a261-0242ac120002", name = "esercizioC3", level = 3)
])

session = Session(id = "72ac49ac-43b8-11ed-b878-0242ac120002", exercises = [
    CognitiveExercise(id = "633d3afa-3cc2-11ed-a261-0242ac120002", name = "esercizioA1", level = 2),
    CognitiveExercise(id = "7d722c82-3cc2-11ed-a261-0242ac120002", name = "esercizioH2", level = 3),
    CognitiveExercise(id = "9177aa04-3cc2-11ed-a261-0242ac120002", name = "esercizioE13", level = 3)
])
#session = easySession
#session = hardSession

@app.get("/session")
async def get_session():
    return session

@app.post("/session", status_code=201)
async def add_sessionResult(sessionResult: SessionResult):
    global session
    session = sessionResult
    return session

@app.post("/session", status_code=201)
async def add_session(session1: Session):
    global session
    session = session1
    return session
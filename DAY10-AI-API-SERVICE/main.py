from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from ai_service import goshugpt

app = FastAPI()


class Question(BaseModel):
    question : str

class Answer(BaseModel):
    question : str 
    answer:str


@app.post("/generate",response_model=Answer)
def generate(question:Question,):
    try:
        result = goshugpt(question.question)
    except ValueError as error:
        raise HTTPException(
            status_code=502,
            detail="gemini returned invalid JSON please Try again later",
        ) from error
    return Answer(
        question=question.question,
        answer=result["answer"],
    )

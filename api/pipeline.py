from fastapi import FastAPI
from pydantic import BaseModel
from agents.writer import generate_spin
from agents.reviewer import review_text
from agents.editor import final_edit

app = FastAPI()

class Chapter(BaseModel):
    content: str

@app.post("/spin")
def spin_text(chapter: Chapter):
    return {"output": generate_spin(chapter.content)}

@app.post("/review")
def review_text_api(chapter: Chapter):
    return {"output": review_text(chapter.content)}

@app.post("/final")
def final_text_api(chapter: Chapter):
    return {"output": final_edit(chapter.content)}

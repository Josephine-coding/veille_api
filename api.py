from fastapi import FastAPI
from afinn import Afinn

app = FastAPI()

afinn = Afinn()

@app.get("/{input}")
def predict(input: str):
    score = afinn.score(input)
    return {'text': input, 'score': score}
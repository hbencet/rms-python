from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np


app = FastAPI()


model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model=model,
    tokenizer=tokenizer
)


class ReviewRequest(BaseModel):
    reviews: list[str]



def convert_stars_to_label(stars: int):
    if stars <= 2:
        return "negatív"
    elif stars == 3:
        return "semleges"
    return "pozitív"


@app.post("/analyze")
def analyze(req: ReviewRequest):

    results = sentiment_pipeline(req.reviews)

    response = []

    for r in results:
        stars = int(r['label'][0])
        label = convert_stars_to_label(stars)

        response.append({
            "label": label,
            "confidence": float(r["score"])
        })

    return {"results": response}



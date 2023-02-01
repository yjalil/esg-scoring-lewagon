import joblib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from esgscoringlewagon.data.preprocessors import BodyPreprocessor
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from esgscoringlewagon.api.models import articleModel, companyModel
from esgscoringlewagon.api.schemas import articleSchema, companySchema
from esgscoringlewagon.api.db.db_setup import get_db, Session
router = APIRouter()
# response_model = articleSchema.ArticlePredictOut

@router.post("/article/predict/",status_code =200)
def predict_article(article: articleSchema.ArticlePredictIn, db: Session = Depends(get_db)):
    topic_model = joblib.load("esgscoringlewagon/api/routers/topic_sgdc_classifier.pkl")
    sentiment_model = SentimentIntensityAnalyzer()
    text = [BodyPreprocessor().fit_transform(article.body)]
    topic_prediction = topic_model.predict(text)
    print(topic_prediction)
    sentiment_prediction = sentiment_model.polarity_scores(text)['compound']
    output = articleSchema.ArticlePredictOut(
        topic_category = topic_prediction[0],
        esg_score = sentiment_prediction
    )
    return output

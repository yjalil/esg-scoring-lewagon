import json
from fastapi.testclient import TestClient

from esgscoringlewagon.api.main import app

client = TestClient(app)

def test_single_article_predict():
    # Create company
    response = client.post("/article/predict/",json={'body':'Those cuts are before a $7,500 U.S. federal tax credit that took effect for many electric vehicles on Jan. 1 that could bring discounts to more than 30%.'})
    assert response.status_code == 200
    assert response.json()['topic_category'] == 'None'
    assert type(response.json()['esg_score']) == float

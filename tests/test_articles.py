import json
from fastapi.testclient import TestClient

from esgscoringlewagon.api.main import app

client = TestClient(app)

def test_create_article_company_inexistant():
    # Create company
    response = client.post("/article/add/no_comp",json={
        "date": "2023-01-23T13:24:37.843Z",
        "title": "string",
        "uploaded_at": "2023-01-23T13:24:37.843Z",
        "body": "string with more than 10 characters",
        "sourceURL": "string",
        "topic_category": "string",
        "esg_score": 0,
        "scored_at": "2023-01-23T13:24:37.843Z",
        "exclude_count": 0
    })
    assert response.status_code == 404

def test_create_article_with_missing_fields():
    # Create company
    response = client.post("/company/add/",json={'name':'test_company_articles_1','description':'test description for test_company_articles_1'})
    assert response.status_code == 201
    # Add article with missing fields
    response = client.post("/article/add/test_company_articles_1",json={
        "date": "2023-01-23T13:24:37.843Z",
        "title": "",
        "uploaded_at": "2023-01-23T13:24:37.843Z",
        "body": "not 10",
        "sourceURL": "string",
        "topic_category": "string",
        "esg_score": 0,
        "scored_at": "2023-01-23T13:24:37.843Z",
        "exclude_count": 0
    })
    assert response.status_code == 422
    # Delete company
    response = client.delete("/company/delete/test_company_articles_1")
    assert response.status_code == 204


def test_create_article():
    response = client.post("/company/add/",json={'name':'test_company_articles_1','description':'test description for test_company_articles_1'})
    assert response.status_code == 201
    # Add article with missing fields
    response = client.post("/article/add/test_company_articles_1",json={
        "date": "2023-01-23T13:24:37.843Z",
        "title": "more than 3",
        "uploaded_at": "2023-01-23T13:24:37.843Z",
        "body": "string with more than 10 characters",
        "sourceURL": "WWW.string.com/stroyURL",
        "topic_category": "TES",
        "esg_score": 0,
        "scored_at": "2023-01-23T13:24:37.843Z",
        "exclude_count": 0
    })
    assert response.status_code == 201
    
    
def test_get_article_by_id():    
    # Get company
    response = client.get("/article/byId/1")
    assert response.status_code == 200
    
def test_get_articles_by_date():    
    # Get company
    response = client.get("/articles/byDate/2023-01-23T13:24:37.843Z")
    assert response.status_code == 200
    
def test_get_articles_by_company():    
    # Get company
    response = client.get("/articles/byCompany/test_company_articles_1")
    assert response.status_code == 200
    
def test_delete_article_parent_company():    
    # Delete company
    response = client.delete("/company/delete/test_company_articles_1")
    assert response.status_code == 204
    response = client.get("/articles/byCompany/test_company_articles_1")
    assert response.status_code == 404
        
    

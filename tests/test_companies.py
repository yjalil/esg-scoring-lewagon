import json
from fastapi.testclient import TestClient

from esgscoringlewagon.api.main import app

client = TestClient(app)

def test_create_no_name_company():
    # Create company
    response = client.post("/company/add/",json={'name':'','description':''})
    assert response.status_code == 422

def test_create_company():
    # Create company
    response = client.post("/company/add/",json={'name':'test_company_1','description':'test description for test_company_1'})
    assert response.status_code == 201
    assert response.json()['name'] == 'test_company_1'
    assert response.json()['description'] == 'test description for test_company_1'
    assert response.json()['id'] != None

def test_create_existing_company():
    # Create company
    response = client.post("/company/add/",json={'name':'test_company_1','description':'test description for test_company_1'})
    assert response.status_code == 409
    

def test_get_company():    
    # Get company
    response = client.get("/companies/test_company_1")
    assert response.status_code == 200
    assert response.json()['name'] == 'test_company_1'
    assert response.json()['description'] == 'test description for test_company_1'
    assert response.json()['id'] != None

def test_update_company_name():    
    # Update company name
    response = client.put("/company/update/test_company_1",json={'name':'test_company_1_updated','description':'test description for test_company_1'})
    assert response.status_code == 200
    assert response.json()['name'] == 'test_company_1_updated'
    assert response.json()['description'] == 'test description for test_company_1'
    assert response.json()['id'] != None

def test_update_company_description():    
    # Update company description
    response = client.put("/company/update/test_company_1_updated",json={'name':'test_company_1_updated','description':'test description for test_company_1_updated'})
    assert response.status_code == 200
    assert response.json()['name'] == 'test_company_1_updated'
    assert response.json()['description'] == 'test description for test_company_1_updated'
    assert response.json()['id'] != None

def test_delete_company():    
    # Delete company
    response = client.delete("/company/delete/test_company_1_updated")
    assert response.status_code == 204

def test_delete_inexistant_company():    
    # Delete company
    response = client.delete("/company/delete/test_company_1_updated")
    assert response.status_code == 404
    
    

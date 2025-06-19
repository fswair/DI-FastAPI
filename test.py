import pytest
import requests

def test_profile():
    url = "http://127.0.0.1:8080/profile"

    headers = {
        "Authorization": "Bearer bearer_venus"
    }
    
    response = requests.get(url, headers=headers, verify=False)
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    print("Response JSON:", response.json())

def test_converter():
    url = "http://127.0.0.1:8080/services/exchange_rates/converter"
    headers = {
        "Authorization": "Bearer bearer_venus"
    }
    params = {
        "try_amount": 1000
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    print("Response JSON:", response.json())
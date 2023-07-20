import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"

def test_1():
    endpoint = f"{BASE_URL}/dishes"

    dishes = ["orange", "spaghetti", "apple pie"]
    response_ids = []

    for dish in dishes:
        payload = {"name": dish}
        response = requests.post(endpoint, json=payload)

        assert response.status_code == 201, "Status code incorrect."

        dish_id = response.text.strip()

        assert dish_id not in response_ids, "Duplicated dish id"
        response_ids.append(dish_id)

def test_2():
    endpoint = f"{BASE_URL}/dishes/1"
    response = requests.get(endpoint)
    assert response.status_code == 200, "Status code incorrect."
    assert 0.9 <= response.json()["sodium"] <= 1.1, "Sodium level incorrect"

def test_3():
    endpoint = f"{BASE_URL}/dishes"
    response = requests.get(endpoint)
    assert response.status_code == 200, "Incorrect status code"
    assert len(response.json()) == 3, "Incorrect amount of json objects"

def test_4():
    endpoint = f"{BASE_URL}/dishes"
    response = requests.post(endpoint, json={"name": "blah"})
    assert response.status_code in [404, 400, 422], "Incorrect status code"
    assert response.json() == -3, "Incorrect returned value"

def test_5():
    endpoint = f"{BASE_URL}/dishes"
    response = requests.post(endpoint, json={"name": "orange"})
    assert response.status_code in [400, 404, 422], "Incorrect status code"
    assert response.json() == -2, "Incorrect returned value"

def test_6():
    endpoint = f"{BASE_URL}/meals"
    response = requests.post(endpoint, json={
        "name": "delicious",
        "appetizer": 1,
        "main": 2,
        "dessert": 3
    })
    assert response.status_code == 201, "Incorrect status code"
    assert response.json() > 0, "Incorrect ID returned"

def test_7():
    endpoint = f"{BASE_URL}/meals"
    response = requests.get(endpoint)
    assert response.status_code == 200, "Incorrect status code"
    assert len(response.json()) == 1, "Incorrect amount of meals"
    assert 400 <= response.json()['1']['cal'] <= 500, "Incorrect amount of calories"

def test_8():
    endpoint = f"{BASE_URL}/meals"
    response = requests.post(endpoint, json={
        "name": "delicious",
        "appetizer": 1,
        "main": 2,
        "dessert": 3
    })
    assert response.status_code in [400, 422], "Incorrect status code"
    assert response.json() == -2, "Incorrect returned value"

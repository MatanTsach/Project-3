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

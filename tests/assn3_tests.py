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

        assert response.status_code == 201, "TEST1: Failed, status code incorrect."

        dish_id = response.text.strip()

        assert dish_id not in response_ids, "TEST1: Failed, duplicated dish id"
        response_ids.append(dish_id)

    print("TEST1: Success")
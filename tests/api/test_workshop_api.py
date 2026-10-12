"""Workshop API tests: verify HTTP responses and database isolation."""

import pytest

pytestmark = pytest.mark.api


def test_post_car_returns_201_and_json(client):
    payload = {
        "make": "Ford",
        "model": "Fiesta",
        "year": 2018,
        "color": "Black",
    }
    response = client.post("/api/cars", json=payload)
    assert response.status_code == 201
    car = response.json()
    assert car["id"] > 0
    assert car["make"] == "Ford"
    assert car["model"] == "Fiesta"
    assert response.headers["location"] == f"/api/cars/{car['id']}"


def test_invalid_year_is_not_saved(client):
    response = client.post(
        "/api/cars",
        json={"make": "Toyota", "model": "Yaris", "year": 1800, "color": "Blue"},
    )
    assert response.status_code == 422
    remaining_cars = client.get("/api/cars")
    assert remaining_cars.status_code == 200
    assert remaining_cars.json() == []

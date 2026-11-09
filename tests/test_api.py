import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_request():
    response = client.post(
        "/monthly-payment",
        json={"principal": 10000, "annual_rate": 0.05, "months": 24},
    )
    assert response.status_code == 200
    assert response.json()["payment"] == pytest.approx(438.71, abs=0.01)


def test_invalid_duration_returns_400():
    response = client.post(
        "/monthly-payment",
        json={"principal": 10000, "annual_rate": 0.05, "months": 0},
    )
    assert response.status_code == 400
    assert "le nb de mois doit etre superieur a 0" in response.json()["detail"]


def test_negative_principal_returns_422():
    response = client.post(
        "/monthly-payment",
        json={"principal": -500, "annual_rate": 0.05, "months": 5},
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "principal"]

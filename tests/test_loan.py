import pytest

from app.loan import monthly_payment


def test_zero_interest():
    # 12 000 sur 12 mois à 0 % : on rembourse simplement 1 000 par mois
    assert monthly_payment(12000, 0.0, 12) == pytest.approx(1000.0)


def test_standard_loan():
    # 10 000 à 5 % annuel sur 24 mois
    assert monthly_payment(10000, 0.05, 24) == pytest.approx(438.71, abs=0.01)


def test_invalid_duration():
    with pytest.raises(ValueError):
        monthly_payment(10000, 0.05, 0)


def test_invalid_duration_zero_rate():
    with pytest.raises(ValueError):
        monthly_payment(10000, 0.0, 0)

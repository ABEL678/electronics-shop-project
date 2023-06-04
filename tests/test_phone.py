import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test_calculate_total_price(phone):
    assert phone.calculate_total_price() == 600000


def test_apply_discount(phone):
    Phone.pay_rate = 0.8
    phone.apply_discount()
    assert phone.price == 96000.0


def test_all():
    assert Phone.all != []


def test_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1 + phone1 == 10

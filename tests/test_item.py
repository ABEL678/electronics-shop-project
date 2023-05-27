"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_all(item1):
    assert Item.all != []


def test_name():
    with pytest.raises(ValueError):
        len('СуперСмартфон Apple14')


def test_instantiate_from_csv() -> None:
    Item.instantiate_from_csv()
    assert len(Item.all) == 10


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'

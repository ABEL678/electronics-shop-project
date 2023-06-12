"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os

import pytest
from src.item import Item, InstantiateCSVError


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


def test_all():
    assert Item.all != []


def test_name(item1):
    with pytest.raises(Exception):
        item1.name = "СуперСмартфонApple14"


def test_instantiate_from_csv() -> None:
    Item.instantiate_from_csv()
    assert len(Item.all) == 10

    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        os.path.join(current_dir, 'items1.csv')
    except FileNotFoundError:
        assert FileNotFoundError == 'Отсутствует файл item.csv'

    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        os.path.join(current_dir, 'items_test.csv')
    except InstantiateCSVError as ex:
        assert ex.message == 'Файл item.csv поврежден'


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + item1 == 40

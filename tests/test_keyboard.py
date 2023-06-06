import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    kb = Keyboard('KD87A', 9600, 5)
    return kb


def test_language(keyboard):
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "EN"


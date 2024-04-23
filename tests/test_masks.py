import pytest

from src.masks import account_masks, card_masks


@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        ("7564234558987552", "7564 23** **** 7552"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_card_masks(card_number: str, expected_result: str) -> None:
    assert card_masks(card_number) == expected_result


@pytest.fixture
def data() -> str:
    return "73654108430135874305"


def test_account_masks(data: str) -> None:
    assert account_masks(data) == "**4305"

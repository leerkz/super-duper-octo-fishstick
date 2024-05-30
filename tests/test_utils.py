import json
import os
from unittest.mock import Mock, patch

from src.utils import data_finance


@patch("builtins.open")
def test_data_finance(mock_open: Mock) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps(
        [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        ]
    )
    assert data_finance(os.path.join("..", "data", "operations.json")) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


def test_data_finance_with_mistake() -> None:
    way = "C:\\Users\\Studentrojects\\pythonProject3\\data\\operations.json"
    assert data_finance(way) == []


def test_get_transactions() -> None:
    mock_random = Mock(return_value=31957.58)
    assert mock_random() == 31957.58

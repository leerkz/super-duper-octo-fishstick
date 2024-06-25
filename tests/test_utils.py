import json
import os
from unittest.mock import Mock, patch

from pandas import DataFrame

from src.utils import data_finance, reading_csv, reading_xlsx


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


@patch("pandas.read_excel")
def test_reading_xlsx(mock_read_excel: Mock) -> None:
    mock_read_excel.return_value = DataFrame({"key": ["value"]})
    assert reading_xlsx("test.xlsx") == [{"key": "value"}]


@patch("pandas.read_csv")
def test_reading_csv(mock_read_excel: Mock) -> None:
    mock_read_excel.return_value = DataFrame({"key": ["value"]})
    assert reading_csv("test.csv") == [{"key": "value"}]

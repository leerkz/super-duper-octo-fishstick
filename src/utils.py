import json
import os
from typing import Any

import requests
from dotenv import load_dotenv


def data_finance(path: str) -> Any:
    """
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(path, "r", encoding="UTF-8") as file:
            read_file = json.load(file)
            return read_file
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def get_transactions(transaction: dict) -> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    """
    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    load_dotenv()
    apikey = os.getenv("API_KEY")
    headers = {"api_key": apikey}
    payload: dict[Any, Any] = {}
    if code != "RUB":
        url = f"https://v6.exchangerate-api.com/v6/{apikey}/latest/USD"
        response = requests.get(url, headers=headers, data=payload)
        currency = response.json()
        usd_eur = currency["conversion_rates"]["RUB"]
        rubles = usd_eur * float(amount)
        return float(rubles)
    else:
        return float(amount)

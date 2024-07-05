import json
import logging
import os
import re
from collections import Counter
from typing import Any

import pandas as pd
import requests
from dotenv import load_dotenv

log = logging.getLogger("utils")
handler = logging.FileHandler("utils.log")
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


def data_finance(path: str) -> Any:
    """
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    """
    log.info(f"start data_finance {path}")
    try:
        with open(path, "r", encoding="UTF-8") as file:
            read_file = json.load(file)
            return read_file
    except FileNotFoundError:
        result2: Any = []
        log.info(f"return result {result2}")
        return result2
    except json.JSONDecodeError:
        result3: Any = []
        log.info(f"return result {result3}")
        return result3


def get_transactions(transaction: dict) -> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    """
    log.info(f"start get_transactions {transaction}")
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
        result1 = float(rubles)
        log.info(f"return result {result1}")
        return result1
    else:
        result2 = float(amount)
        log.info(f"return result {result2}")
        return result2


def reading_csv(file_path: Any) -> list[Any]:
    """
    считывание финансовых операций с CSV-файлов.
    """
    csv_reviews = pd.read_csv(file_path, sep=";")
    convert = csv_reviews.to_dict(orient="records")
    return convert


def reading_xlsx(file_path: Any) -> list[Any]:
    """
    считывание финансовых операций с XLSX-файлов.
    """
    xlsx_reviews = pd.read_excel(file_path)
    convert = xlsx_reviews.to_dict(orient="records")
    return convert


def sorted_by_line(bank_operate: list[dict], search_line: str) -> list[dict]:
    """
    Принимает данные о банковских операциях и строку поиска и возвращет список словарей с описаниум данной строки.
    """
    pattern = re.compile(search_line, re.I)
    result_answer = []
    for element in bank_operate:
        if pattern.search(element["description"]):
            result_answer.append(element)
    return result_answer


def get_amount_by_category(bank_operate: list[dict], descriptions: dict) -> dict:
    """
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций категории.
    """
    pattern1 = re.compile("Перевод организации", re.I)
    pattern2 = re.compile("Перевод с карты на карту", re.I)
    pattern3 = re.compile("Перевод со счета на счет", re.I)
    pattern4 = re.compile("Открытие вклада", re.I)
    counter = Counter(operation["description"] for operation in bank_operate)
    descriptions["Перевод организации"] = counter[pattern1.pattern]
    descriptions["Перевод с карты на карту"] = counter[pattern2.pattern]
    descriptions["Перевод со счета на счет"] = counter[pattern3.pattern]
    descriptions["Открытие вклада"] = counter[pattern4.pattern]
    return descriptions

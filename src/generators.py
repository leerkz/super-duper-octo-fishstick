from typing import Iterator


def filter_by_currency(transact: list[dict], value: str) -> Iterator:
    """
    Выдает по очереди операции, в которых указана заданная валюта.

    """
    for item in transact:
        if item["operationAmount"]["currency"]["code"] == value:
            yield item


def transaction_descriptions(transact: list[dict]) -> Iterator:
    """
    Возвращает описание каждой операции по очереди.

    """
    for symbol in transact:
        yield symbol["description"]


def number_generator(beginning: int, finish: int) -> Iterator:
    """
    Генерирует номера карт.

    """
    for num in range(beginning, finish + 1):
        str_ = "0" * (16 - len(str(num))) + str(num)
        yield f"{str_[0:4]} {str_[4: 8]} {str_[8: 12]} {str_[12: 16]}"

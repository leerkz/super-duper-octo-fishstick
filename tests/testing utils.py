from src.masks import account_masks, card_masks
from src.widget import card_account

try:

    print(card_masks("7564234558987552"))
except TypeError:
    print("Найдена ошибка")
else:
    print("Функция, возвращающая маску карты, справилась и со строками, и с числами")

try:

    print(account_masks("73654108430135874305"))
except TypeError:
    print("Найдена ошибка")
else:
    print("Функция, возвращающая маску счета, справилась и со строками, и с числами")

test = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

for i in test:
    print(card_account(i))

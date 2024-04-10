from src.masks import account_masks, card_masks

try:
    print(card_masks(7564234558987552))
    print(card_masks("7564234558987552"))
except TypeError:
    print("Найдена ошибка")
else:
    print("Функция, возвращающая маску карты, справилась и со строками, и с числами")

try:
    print(account_masks(73654108430135874305))
    print(account_masks("73654108430135874305"))
except TypeError:
    print("Найдена ошибка")
else:
    print("Функция, возвращающая маску счета, справилась и со строками, и с числами")

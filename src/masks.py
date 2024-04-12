def card_masks(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    return str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]


def account_masks(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    return "**" + str(account_number)[-4:]

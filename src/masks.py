import logging

log = logging.getLogger("masks")
handler = logging.FileHandler("masks.log")
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


def card_masks(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    log.info(f"start card_masks {card_number}")
    result = str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]
    log.info(f"mask {result}")
    return result


def account_masks(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    log.info(f"start account_masks {account_number}")
    result = "**" + account_number[-4:]
    log.info(f"mask {result}")
    return result

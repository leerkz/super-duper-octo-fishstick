from src.masks import account_masks, card_masks


def card_account(card: str) -> str:
    """
    Возвращает исходную строку с замаскированным номером карты/счета.

    """
    alpha = ""
    digit = ""
    for symbol in card:
        if symbol.isalpha() or symbol == " ":
            alpha += symbol
        elif symbol.isdigit():
            digit += symbol
    if alpha.strip() == "Счет":

        return alpha.strip() + " " + account_masks(digit)
    else:

        return alpha.strip() + " " + card_masks(digit)


def date(data_date: str) -> str:
    """
    Фильтрует дату.

    """
    list_data = data_date.split("-")
    list_data[-1] = list_data[-1].split("T")[0]
    return ".".join(list_data[::-1])


# print(date("2018-07-11T02:26:18.671407"))
# print(card_account("Visa Platinum 7000 7922 8960 6361"))

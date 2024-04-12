def card_account(card: str) -> str:
    alpha = ""
    digit = ""
    for symbol in card:
        if symbol.isalpha() or symbol == " ":
            alpha += symbol
        elif symbol.isdigit():
            digit += symbol
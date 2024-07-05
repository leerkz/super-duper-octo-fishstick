def leaves_dict(dict_list: list, state: str = "EXECUTED") -> list:
    """
    оставляет те словари, которые задал пользователь.

    """
    new_list = []
    for item in dict_list:
        if item.get("state", "") == state:
            new_list.append(item)
    return new_list


def sorted_dict_date(dict_list: list, reverse: bool = False) -> list:
    """
    сортирует словари по дате.

    """
    new_list = sorted(dict_list, key=lambda x: x.get("date", ""), reverse=reverse)
    return new_list

import os.path

from src.processing import leaves_dict, sorted_dict_date
from src.utils import data_finance, reading_csv, reading_xlsx, sorted_by_line

from src.widget import card_account, date


def main() -> None:
    """
    Основная функция.
    """
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакициями."
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла"""
    )
    user_input = input()
    if user_input == "1":
        print("Для обработки выбран json файл.")
        data = data_finance(os.path.join("data", "operations.json"))
    elif user_input == "2":
        print("Для обработки выбран csv файл.")
        data = reading_csv(os.path.join("data", "transactions.csv"))
    else:
        print("Для обработки выбран xlsx файл.")
        data = reading_xlsx(os.path.join("data", "transactions_excel.xlsx"))
    while True:
        print(
            "Введите статус по которому необходимо выполнить фильтрацию."
            """Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )

        input2 = input().upper()
        if input2 == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
            data = leaves_dict(data, "EXECUTED")
            break
        elif input2 == "CANCELED":
            print('Операции отфильтрованы по статусу "CANCELED"')
            data = leaves_dict(data, "CANCELED")
            break
        elif input2 == "PENDING":
            print('Операции отфильтрованы по статусу "PENDING"')
            data = leaves_dict(data, "PENDING")
            break
        else:
            print(f"Статус операции {input2} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")
    input3 = input().lower()
    if input3 == "да":
        print("Отсортировать по возрастанию или по убыванию? ")
        input4 = input().lower()
        if "возраст" in input4:
            data = sorted_dict_date(data)
        else:
            data = sorted_dict_date(data, True)
    print("Выводить только рублевые тразакции?ll Да/Нет")
    input5 = input().lower()
    if input5 == "да":
        new_list = []
        for i in data:
            if user_input == "1":
                if i.get("operationAmount", {}).get("currency", {}).get("code", "") == "RUB":
                    new_list.append(i)
            else:
                if i.get("currency_code", "") == "RUB":
                    new_list.append(i)

        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        input6 = input().lower()
        if input6 == "да":
            print("Введите слово, по которому хотите отсортировать списки")
            input7 = input()

            data = sorted_by_line(new_list, input7)
        elif input6 == "нет":
            data = new_list

        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(data)}")

        if len(data) == 0:
            print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")
        else:
            for transaction in data:
                if isinstance(transaction.get("from", None), float) or isinstance(transaction["to"], float):
                    continue
                else:
                    print(
                        f"""{date(transaction['date'])} {transaction['description']}
{card_account(transaction['from'])} -> {card_account(transaction['to'])}
{int(transaction.get('amount', 0))} руб."""
                    )
    else:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        input6 = input().lower()
        if input6 == "да":
            print("Введите слово, по которому хотите отсортировать списки")
            input7 = input()

            new_data = sorted_by_line(data, input7)
        elif input6 == "нет":
            new_data = data

        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(new_data)}")

        if len(new_data) == 0:
            print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")
        else:
            for transaction in data:
                if isinstance(transaction.get("from", None), float) or isinstance(transaction["to"], float):
                    continue
                else:
                    print(
                        f"""{date(transaction['date'])} {transaction['description']}
        {card_account(transaction.get('from', "None"))} -> {card_account(transaction['to'])}
        {int(transaction.get('amount', 0))} руб."""
                    )


if __name__ == "__main__":
    main()

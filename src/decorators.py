from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Логирует вызов функции и ее результат в файл или в консоль.

    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            if filename is None:
                try:
                    result = func(*args, **kwargs)
                except Exception as type_error:
                    print(f"{func.__name__} error {type_error} Input{args, kwargs}")
                else:
                    print(f"{func.__name__} ok")
                    return result
            else:
                try:
                    result = func(*args, **kwargs)
                except Exception as type_error:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} error {type_error} Input{args, kwargs}\n")
                else:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok\n")

                    return result

        return inner

    return wrapper

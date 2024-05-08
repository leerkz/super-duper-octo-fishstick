import pytest

from src.decorators import log


@log("mylog.txt")
def decorators(x: int, y: int) -> int:
    return x + y


@pytest.mark.parametrize(
    "x, y, answer",
    [
        (1, 2, "decorators ok"),
        (1, "2", "decorators error unsupported operand type(s) for +: 'int' and 'str' Input((1, '2'), {})"),
    ],
)
def test_log(x: int, y: int | str, answer: str) -> None:
    decorators(x, y)
    with open("mylog.txt", "r", encoding="utf8") as file:
        for line in file:
            pass
    assert line.strip() == answer

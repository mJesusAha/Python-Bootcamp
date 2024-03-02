# Задание 3
# python3  exs02.py
from typing import Dict


def my_decorator(func):
    print("SQUEAK")
    return func


# Проверяет если в словаре gold_ingots, и если нет,
# то возвращает новый пустрой


def check_ingot(purse_):
    if "gold_ingots" in purse_:
        return purse_
    else:
        purse_ = {"gold_ingots": 0}
        return purse_


# Добавляет 1 слиток
@my_decorator
def add_ingot(purse_):
    purse = check_ingot(purse_)

    if purse["gold_ingots"] < 0:
        purse["gold_ingots"] = 0
    purse["gold_ingots"] += 1
    return purse


# Вытаскивает 1 слиток
@my_decorator
def get_ingot(purse_):
    purse = check_ingot(purse_)
    if purse["gold_ingots"] > 0:
        purse["gold_ingots"] -= 1
    else:
        purse["gold_ingots"] = 0
    return purse


# Опустошает кошелек
@my_decorator
def empty(purse_):
    # purse = check_ingot(purse_)
    purse = {"gold_ingots": 0}
    return purse


if __name__ == "__main__":
    purse = Dict[str, int]
    purse = {"gold_ingots": 6}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))
    print(purse)
    purse = add_ingot(get_ingot(add_ingot(purse)))
    print(purse)
# # ////////////////////////////////////////////////////

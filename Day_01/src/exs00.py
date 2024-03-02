# день 01
# black --line-length=79 exs00.py
# python3  exs00.py
# ///////////////////////////////////////////////
# задание 1
from typing import Dict


# Проверяет если в словаре gold_ingots, и если нет,
# то возвращает новый пустрой
def check_ingot(purse_):
    if "gold_ingots" in purse_:
        return purse_
    else:
        purse_ = {"gold_ingots": 0}
        return purse_


# Добавляет 1 слиток
def add_ingot(purse_):
    purse = check_ingot(purse_)

    if purse["gold_ingots"] < 0:
        purse["gold_ingots"] = 0

    purse["gold_ingots"] += 1
    return purse


# Вытаскивает 1 слиток
def get_ingot(purse_):
    purse = check_ingot(purse_)
    if purse["gold_ingots"] > 0:
        purse["gold_ingots"] -= 1
    else:
        purse["gold_ingots"] = 0
    return purse


# Опустошает кошелек
def empty(purse_):
    purse = check_ingot(purse_)
    purse["gold_ingots"] = 0
    return purse


if __name__ == "__main__":
    purse = Dict[str, int]

    print(add_ingot(get_ingot(add_ingot(empty(purse)))))
# ////////////////////////////////////////////////////

# Задание 2
# python3  exs01.py
from typing import Dict


def split_booty(*argv):
    sum = 0
    wallet1, wallet2, wallet3 = (
        {"gold_ingots": 0},
        {"gold_ingots": 0},
        {"gold_ingots": 0},
    )
    for i in range(len(argv)):
        if "gold_ingots" in argv[i]:
            if argv[i]["gold_ingots"] >= 0:
                sum += argv[i]["gold_ingots"]
    x = sum // 3
    wallet1["gold_ingots"] = wallet2["gold_ingots"] = wallet3[
        "gold_ingots"
    ] = x
    if (sum - (x * 3)) > 0:
        wallet1["gold_ingots"] += 1
    if sum - x * 3 > 1:
        wallet2["gold_ingots"] += 1
    return wallet1, wallet2, wallet3


# # Написать тест из этого
if __name__ == "__main__":
    wallet1 = {"gold_ingots": 3}
    wallet3 = {"gold_ingots": 2}
    wallet2 = {"apple": 10}

    n = split_booty(wallet1, wallet2, wallet3)
    print(n)

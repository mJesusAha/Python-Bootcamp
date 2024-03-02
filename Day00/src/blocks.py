# 1-e задание 0 день
# cat data_hashes_10lines.txt | python3 blocks.py 10
from sys import stdin, argv


def f(n):
    lines = []
    for line in stdin:
        lines.append(line.rstrip("\n"))
    if len(n) < 2 or n[1].isdigit() == False:
        t = 0
    else:
        t = n[1]
    return lines[0 : int(t)]


def f1(lines):
    for i in range(len(lines)):
        if (
            len(lines[i]) == 32
            and lines[i][5] != "0"
            and lines[i].count("00000")
        ):
            print(lines[i])


if __name__ == "__main__":
    f1(f(argv))

# 3-e задание 0 день
# black --line-length=79 mfinder.py
# cat m.txt | python3 mfinder.py
from sys import stdin, argv
import re


def f():
    lines = []
    for line in stdin:
        lines.append(line.rstrip("\n"))

    if not (
        len(lines) == 3
        and (len(lines[1]) == len(lines[2]) == len(lines[0]) == 5)
    ):
        print("ERROR")
    else:
        line_1 = re.search(r"[\*][^\*][^\*][^\*][\*]", lines[0])
        line_2 = re.search(r"[\*][\*][^\*][\*][\*]", lines[1])
        line_3 = re.search(r"[\*][^\*][\*][^\*][\*]", lines[2])
        if (line_1) and (line_2) and (line_3):
            print("True")
        else:
            print("False")


if __name__ == "__main__":
    f()

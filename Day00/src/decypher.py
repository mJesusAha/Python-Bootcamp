# 2-e задание 0 день
# black --line-length=79 decypher.py
# python3 decypher.py "Have you delivered eggplant pizza at restored keep?"
from sys import argv


def function(text):
    if len(text) <= 1:
        return
    text_copy = text[1]
    text_copy = text_copy.title()
    first_char = ""
    for i in range(len(text_copy)):
        if text_copy[i].isupper():
            first_char += text[1][i]
    print(first_char)


function(argv)

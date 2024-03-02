# python3 pressure.py   
import random
import time


def my_prints(a):
    t = 100 - a
    spusk = ""
    if a < 10 or a > 90:
        spusk = spusk + "..)o)O)O)"
    color = "\033[31m" if (a <= 20 or a > 80) else "\033[32m"
    print("\033c", end="")
    print(
        "\n\n" + "\t" * 6 + "  " + str(a) + "\n" + "-" * 102 + "\n" + "|",
        color + "|" * a + "\033[0m " * t + "|" + spusk + "\n" + "-" * 102,
        sep="",
    )
    print(
        "0 "
        + "_" * 7
        + " 10 "
        + "_" * 6
        + " 20 "
        + "_" * 26
        + " 50 "
        + "_" * 26,
        "80 " + "_" * 6 + " 90 " + "_" * 5 + " 100\n\n",
    )
    if a < 10 or a > 90:
        time.sleep(2)
        print("\033c", end="")
        print(
            "\n\t " + "*" * 15 + "\n\t **" + "-" * 11 + "** \n"
            "\t" + " **  The end  **",
            "\n\t **" + "-" * 11 + "** \n\t " + "*" * 15 + "\n\n",
        )


def valve(self):
    for i in self:
        if i > 80:
            self.send(-1)
        if i <= 20:
            self.send(1)


def emit_gel(step_):
    print("\033c", end="")
    step = random.randint(1, step_)
    i_ = 0
    sign1 = 1
    while True:
        a = 50 + i_
        sign = yield a
        if sign != None and int(sign) < 0:
            sign1 = -1
        if sign != None and int(sign) > 0:
            sign1 = 1
        step = random.randint(1, step_)
        time.sleep(1)
        i_ += step * sign1
        if a > 100:
            a = 50
        if a < 0:
            a = 0
        yield a

        my_prints(a)
        if a < 10 or a > 90:
            break

if __name__ == "__main__":
    n = emit_gel(20)
    valve(n)
    # for i in n:
    #     i

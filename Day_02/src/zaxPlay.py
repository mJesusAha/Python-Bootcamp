# python3 zaxPlay.py
from zax import *

if __name__ == "__main__":
    t = (1, 2, 3, 4, 5)
    n = Game(10, t)
    n.play()
    n.result_all()
    n.top3()
    t = Start.starts()
    n = Game(10, t)
    n.play()
    n.result_all()
    n.top3()

# python3 energy.py
from other import *


def fix_wiring(cables, sockets, plugs):
    return fix_wiring1(cables, sockets, plugs)


# |||||||||||||||||||||||||||||
if __name__ == "__main__":
    print("\n")
    plugs = ["plug1", "plug2", "plug3", "tt"]
    sockets = ["socket1", "socket2", "socket3", "socket4"]
    cables = ["cable1", "cable2", "cable3", "cable4"]
    for c in fix_wiring(cables, sockets, plugs):
        print(c)

    print("\n")

    plugs = ["plugZ", None, "plugY", "plugX"]
    sockets = [1, "socket1", "socket2", "socket3", "socket4"]
    cables = ["cable2", "cable1", False]
    for c in fix_wiring(cables, sockets, plugs):
        print(c)

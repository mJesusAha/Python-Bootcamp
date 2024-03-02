# python3 test.py
import unittest
from zax import *
from EX00 import *

from typing import Dict


class TestPassword(unittest.TestCase):
    def test_1(self):
        key: MyKey
        key = MyKey("1")
        self.assertEqual(len(key), 1)
        self.assertEqual(key[404], "1")
        self.assertEqual(key.passphrase, "1")
        self.assertEqual(str(key), "1")
        self.assertEqual(key > 9000, False)

    def test_2(self):
        print("\n")
        key: MyKey
        key = MyKey("zax2rulez")
        self.assertEqual(len(key), 1337)
        self.assertEqual(int(key[404]), 3)
        self.assertEqual(key.passphrase, "zax2rulez")
        self.assertEqual(str(key), "GeneralTsoKeycard")
        self.assertEqual(key > 9000, True)

    def test_3(self):
        key: MyKey
        key = MyKey("zax")
        self.assertEqual(len(key), 1337)
        self.assertEqual(key[404], "x")
        self.assertEqual(key.passphrase, "zax")
        self.assertEqual(str(key), "zax")
        self.assertEqual(key > 9000, False)

    def test_4(self):
        print("\n")
        key: MyKey
        key = MyKey("zax2")
        self.assertEqual(len(key), 1337)
        self.assertEqual(int(key[404]), 3)
        self.assertEqual(key.passphrase, "zax2")
        self.assertEqual(str(key), "zax2")
        self.assertEqual(key > 9000, False)

    def test_5(self):
        print("\n")
        key: MyKey
        key = MyKey("rulez")
        self.assertEqual(len(key), 5)
        self.assertEqual(key[404], "z")
        self.assertEqual(key.passphrase, "rulez")
        self.assertEqual(str(key), "rulez")
        self.assertEqual(key > 9000, True)

    def test_6(self):
        print("\n")
        key: MyKey
        key = MyKey("9001")
        self.assertEqual(len(key), 4)
        self.assertEqual(key[404], "1")
        self.assertEqual(key.passphrase, "9001")
        self.assertEqual(str(key), "9001")
        self.assertEqual(key > 9000, True)


class TestGame_00(unittest.TestCase):
    def test_game1(self):
        t = (1, 2, 3, 4, 5)
        n = Game(10, t)
        n.play()
        n = n.result_all()
        self.assertEqual(n, {3: 57, 4: 46, 1: 45, 5: 45, 2: 29, 6: 0, 7: 0})
        print("\n")

    def test_game2(self):
        t = (1, 2, 3, 4, 5, 6)
        n = Game(10, t)
        n.play()
        n = n.result_all()
        self.assertEqual(n, {6: 81, 3: 74, 4: 63, 5: 60, 1: 48, 2: 46, 7: 0})
        print("\n")


if __name__ == "__main__":
    unittest.main()

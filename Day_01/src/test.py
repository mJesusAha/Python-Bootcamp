# python3  test.py
import unittest

from exs00 import *
from exs01 import *

# from exs02 import *
from typing import Dict


class TestExs_00(unittest.TestCase):
    def test_one_param(self):
        purse = Dict[str, int]
        n = add_ingot(get_ingot(add_ingot(empty(purse))))
        self.assertEqual(n, {"gold_ingots": 1})

    def test_one_param_1(self):
        purse = {"gold": 3}
        n = add_ingot(get_ingot(add_ingot(empty(purse))))
        self.assertEqual(purse, {"gold": 3})
        self.assertEqual(n, {"gold_ingots": 1})


class TestAdd(unittest.TestCase):
    def test_add_ignot_purse_0(self):
        purse = Dict[str, int]
        n = add_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 1})

    def test_add_ignot_purse_1(self):
        purse = {"gold": 1}
        n = add_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 1})

    def test_add_ignot_purse_2(self):
        purse = {"gold_ingots": 1}
        n = add_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 2})

    def test_add_ignot_purse_3(self):
        purse = {"gold_ingots": -2}
        n = add_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 1})

    def test_add_ignot_purse_4(self):
        purse = {"gold_ingots": 4}
        n = add_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 5})


class TestGet(unittest.TestCase):
    def test_get_ignot_purse_0(self):
        purse = Dict[str, int]
        n = get_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 0})

    def test_get_ignot_purse_1(self):
        purse = {"gold": 1}
        n = get_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 0})

    def test_get_ignot_purse_2(self):
        purse = {"gold_ingots": 1}
        n = get_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 0})

    def test_get_ignot_purse_3(self):
        purse = {"gold_ingots": -2}
        n = get_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 0})

    def test_get_ignot_purse_4(self):
        purse = {"gold_ingots": 4}
        n = get_ingot(purse)
        self.assertEqual(n, {"gold_ingots": 3})


class TestEmpty(unittest.TestCase):
    def test_empty_ignot_purse_0(self):
        purse = Dict[str, int]
        n = empty(purse)
        self.assertEqual(n, {"gold_ingots": 0})

    def test_empty_ignot_purse_1(self):
        purse = {"gold": 1}
        n = empty(purse)
        self.assertEqual(n, {"gold_ingots": 0})

    def test_empty_ignot_purse_2(self):
        purse = {"gold_ingots": 1}
        n = empty(purse)
        self.assertEqual(n, {"gold_ingots": 0})

    def test_empty_ignot_purse_3(self):
        purse = {"gold_ingots": -2}
        n = empty(purse)
        self.assertEqual(n, {"gold_ingots": 0})

    def test_empty_ignot_purse_4(self):
        purse = {"gold_ingots": 4}
        n = empty(purse)
        self.assertEqual(n, {"gold_ingots": 0})


class TestExs_01(unittest.TestCase):
    def test_one(self):
        wallet1 = {"gold_ingots": 3}
        n = split_booty(wallet1)
        self.assertEqual(
            n, ({"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 1})
        )

    def test_1(self):
        wallet1 = {"gold_ingots": 3}
        n = split_booty(wallet1)
        self.assertEqual(
            n, ({"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 1})
        )

    def test_1_1(self):
        wallet1 = {"gold_ingots": 0}
        n = split_booty(wallet1)
        self.assertEqual(
            n, ({"gold_ingots": 0}, {"gold_ingots": 0}, {"gold_ingots": 0})
        )

    def test_1_1(self):
        wallet1 = {"gold_ingots": 5}
        n = split_booty(wallet1)
        self.assertEqual(
            n, ({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1})
        )

    def test_1_2(self):
        wallet1 = {"gold_ingots": -2}
        n = split_booty(wallet1)
        self.assertEqual(
            n, ({"gold_ingots": 0}, {"gold_ingots": 0}, {"gold_ingots": 0})
        )

    def test_2(self):
        wallet1 = {"gold_ingots": 3}
        wallet2 = {"gold_ingots": 3}
        n = split_booty(wallet1, wallet2)
        self.assertEqual(
            n, ({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 2})
        )

    def test_2_1(self):
        wallet1 = {"gold_ingots": 1}
        wallet2 = {"gold_ingots": 3}
        n = split_booty(wallet1, wallet2)
        self.assertEqual(
            n, ({"gold_ingots": 2}, {"gold_ingots": 1}, {"gold_ingots": 1})
        )

    def test_2_2(self):
        wallet1 = {"gold_ingots": -3}
        wallet2 = {"gold_ingots": 3}
        n = split_booty(wallet1, wallet2)
        self.assertEqual(
            n, ({"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 1})
        )

    def test_2_3(self):
        wallet1 = {"gold_ingots": -3}
        wallet2 = {"gold_ingots": -3}
        n = split_booty(wallet1, wallet2)
        self.assertEqual(
            n, ({"gold_ingots": 0}, {"gold_ingots": 0}, {"gold_ingots": 0})
        )

    def test_3(self):
        wallet1 = {"gold_ingots": 3}
        wallet2 = {"apple": 10}
        wallet3 = {"gold_ingots": 2}

        n = split_booty(wallet1, wallet2, wallet3)
        self.assertEqual(
            (wallet1, wallet2, wallet3),
            ({"gold_ingots": 3}, {"apple": 10}, {"gold_ingots": 2}),
        )
        self.assertEqual(
            n, ({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1})
        )

    def test_3_1(self):
        wallet1 = {"apple": 1}
        wallet2 = {"apple": 10}
        wallet3 = {"gold_ingots": 2}
        wallet4 = {"gold_pants": 2}
        wallet5 = {"gold_ingots": -5}
        wallet6 = {"gold_ingots": 4}
        wallet7 = Dict[str, int]
        wallet8 = {"gold_ingots": 12}
        n = split_booty(wallet1, wallet2)
        self.assertEqual(
            n, ({"gold_ingots": 0}, {"gold_ingots": 0}, {"gold_ingots": 0})
        )
        n = split_booty(wallet1, wallet2, wallet3, wallet4, wallet5)
        self.assertEqual(
            n, ({"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 0})
        )
        n = split_booty(wallet1, wallet2, wallet3)
        self.assertEqual(
            n, ({"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 0})
        )
        n = split_booty(
            wallet1,
            wallet2,
            wallet3,
            wallet4,
            wallet5,
            wallet6,
            wallet7,
            wallet8,
        )
        self.assertEqual(
            n, ({"gold_ingots": 6}, {"gold_ingots": 6}, {"gold_ingots": 6})
        )


if __name__ == "__main__":
    unittest.main()

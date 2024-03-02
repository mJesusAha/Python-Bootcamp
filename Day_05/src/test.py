from credentials import *
import unittest


class Test_00(unittest.TestCase):
    def test1(self):
        n = {"specie": ["Time Lord"], "?species": ["Sontaran"]}
        d = search_form(n)
        self.assertEqual(d[1], 0)
        self.assertEqual(d[0], '{"credentials": "Unknown"}')

    def test2(self):
        n = {"specie": ["Time Lord"], "species": ["Sontaran"]}
        d = search_form(n)
        self.assertEqual(d[1], 1)
        self.assertEqual(d[0], '{"credentials": "General Staal"}')

    def test3(self):
        n = {"species": ["Time Lord", "Sontaran"]}
        d = search_form(n)
        self.assertEqual(d[1], 1)
        self.assertEqual(d[0], '{"credentials": "Rassilon, General Staal"}')

    def test4(self):
        n = {"species": ["ffd"]}
        d = search_form(n)
        self.assertEqual(d[1], 0)
        self.assertEqual(d[0], '{"credentials": "Unknown"}')

    def test5(self):
        n = {"species": ["ffd", "Time Lord"]}
        d = search_form(n)
        self.assertEqual(d[1], 1)
        self.assertEqual(d[0], '{"credentials": "Rassilon"}')

    def test6(self):
        n = {"species": ["Sontaran", "ffd", "ffdd", "Time Lord"]}
        d = search_form(n)
        self.assertEqual(d[1], 1)
        self.assertEqual(d[0], '{"credentials": "General Staal, Rassilon"}')

    def test7(self):
        n = {"species": ["Sontaan", "ffd", "ffdd", "Sontaran", "Time Lord", "Human"]}
        d = search_form(n)
        self.assertEqual(d[1], 1)
        self.assertEqual(
            d[0], '{"credentials": "General Staal, Rassilon, Leonardo da Vinci"}'
        )

    def test8(self):
        n = {
            "species": [
                "Sontaan",
                "ffd",
                "ffdd",
                "Sontaran",
                "Time Lord",
                "Human",
                "ffdhd",
            ]
        }
        d = search_form(n)
        self.assertEqual(d[1], 1)
        self.assertEqual(
            d[0], '{"credentials": "General Staal, Rassilon, Leonardo da Vinci"}'
        )

    def test9(self):
        n = {"species": []}
        d = search_form(n)
        self.assertEqual(d[1], 0)
        self.assertEqual(d[0], '{"credentials": "Unknown"}')

    def test10(self):
        n = {"species": ["Sontaran", "ffd", "Time Lord"]}
        d = search_form(n)
        self.assertEqual(d[1], 1)
        self.assertEqual(d[0], '{"credentials": "General Staal, Rassilon"}')

    n = {"species": ["Sontaran", "ffd", "Time Lord"]}


if __name__ == "__main__":
    unittest.main()

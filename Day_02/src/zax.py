# python3 zax.py
from collections import Counter
from time import *


class Game(object):
    def __init__(self, matches=10, *arg):
        arg = arg[0]
        self.arg = arg
        self.matches = matches
        self.registry = Counter()
        self.n = 7  # Количество игоков в системе

    def play(self):
        self.for_player_7()
        self.matrix_game()
        self.games_play()

    def top3(self):
        self.registry = Counter(
            {
                "cheater": self.score[1],
                "cooperator": self.score[2],
                "copycat": self.score[3],
                "granger": self.score[4],
                "you version": self.score[7],
                "detectiv": self.score[5],
                "my": self.score[6],
            }
        )
        n = list(self.registry.most_common(3))
        print(n[0][0], n[0][1])
        print(n[1][0], n[1][1])
        print(n[2][0], n[2][1])

    def matrix_game(self):
        self.score = Counter({1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0})
        self.game_matrix = [[1] * self.n for _ in range(self.n)]
        # Матрица игр
        # 0 - играет 1 - не играет
        for i in range(self.n):
            for j in range(self.n):
                if (
                    self.arg.count(i + 1) and self.arg.count(j + 1)
                ) and i != j:
                    self.game_matrix[i][j] = 0
                    self.game_matrix[j][i] = 0
                if self.game_matrix[i][j] == 0:
                    self.game_matrix[j][i] = 1

    def games_play(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.game_matrix[i][j] == 0:
                    self.play1(i + 1, j + 1)

    def for_player_7(self):
        self.candys = ["0"] * self.matches
        if self.arg.count(7):
            match = 0
            print("\033c", end="")
            while match != self.matches:
                print("\033c", end="")
                print("Введи дашь конфет?, 1-да или 0-нет", match + 1, ": ")
                temp = input()
                while (temp.isdigit() == False) or (
                    temp.isdigit() == True and (int(temp) > 1 or int(temp) < 0)
                ):
                    print("Oшибка ввода. Введи сколько дашь конфет, 0 или 1")
                    temp = input()
                if int(temp) == 1 or int(temp) == 0:
                    text = "дам"
                    if int(temp) == 1:
                        text = "дам"
                    if int(temp) == 0:
                        text = "не дам"

                    print("записано", text)
                    sleep(1)
                    if int(temp) == 1:
                        self.candys[match] = 2
                    else:
                        self.candys[match] = int(temp)

                match += 1
            print("\033c", end="")

            print("Ты ввëл:", end=" ")

            for i in range(self.matches):
                if self.candys[i] == 0:
                    print("зажал", end=" ")
                else:
                    print("дам", end=" ")
            print()
            sleep(3)
            print("\033c", end="")
            print("\tresult:")

    def play1(self, player1, player2):
        # print("(", player1, "  ", player2, "))")
        score = self.one_matche(player1, player2)
        self.score[player1] += score[0]
        self.score[player2] += score[1]

    def one_matche(self, player1, player2):
        self.match = 0
        candy1, candy2, score_p1, score_p2 = 2, 2, 0, 0
        self.flags = {
            "flags1": 0,
            "flags2": 0,
            "candy_p1": 2,
            "candy_p2": 2,
            "match_c_c": 0,
        }
        if player1 == 1:
            candy1 = 0
            self.flags["candy_p1"] = candy1
        if player2 == 1:
            candy2 = 0
            self.flags["candy_p2"] = candy2

        while self.match != self.matches:  # 10
            if player2 == 7:
                candy2 = self.candys[self.match]
                self.flags["candy_p2"] = candy2
            if player1 == 7:
                candy1 = self.candys[self.match]
                self.flags["candy_p1"] = candy1

            p1 = self.choice_player(player1, candy2)
            p2 = self.choice_player(player2, candy1)

            self.flags["candy_p1"] = p1[1]
            self.flags["candy_p2"] = p2[1]
            score_p1 += p1[0]
            candy1 = p1[1]
            score_p2 += p2[0]
            candy2 = p2[1]

            self.match += 1
        return score_p1, score_p2

    def choice_player(self, player, candy):
        if player == 1:
            return Players.Cheater.add_candy(candy)
        if player == 2:
            return Players.Cooperator.add_candy(candy)
        if player == 3:
            return Players.CopyCat.add_candy(candy, self.flags)
        if player == 4:
            return Players.Gradger.add_candy(candy, self.match, self.flags)
        if player == 5:
            return Players.Detectitve.add_candy(candy, self.match, self.flags)
        if player == 7:
            return Players.My.add_candy(candy, self.flags)
        if player == 6:
            return Players.MyCopyCat.add_candy(candy, self.match, self.flags)
        return 0

    def result_all(self):
        return self.score


class Players(object):
    class Cheater(object):
        """Всегда 0"""

        def add_candy(candy):
            score = 0
            if candy == 2:
                score = 3
            return score, 0

    class Cooperator(object):
        """Всегда 1"""

        def add_candy(candy):
            score = -1
            if candy == 2:
                score = 2
            return score, 2

    class CopyCat(object):
        """Первый раз как кооператор, а дальше копирует ходы игрока"""

        def add_candy(candy_, flags):
            if flags["match_c_c"] == 0:
                n = list(Players.Cooperator.add_candy(candy_))
                if candy_ != 2:
                    flags["flags1"] = 1
                    candy = 0
            if flags["match_c_c"] == 0:
                flags["match_c_c"] = 1
                return n[0], candy_
            candy = int(candy_)
            score = 0
            sum_p_p = int(flags["candy_p1"]) + int(flags["candy_p2"])
            if candy == 2 and sum_p_p == 4:
                return 2, candy
            elif candy == 2 and sum_p_p == 2:
                return 3, candy
            elif candy == 0 and sum_p_p == 2:
                return -1, candy
            return score, 0

    class MyCopyCat(object):
        """Первый раз как кооператор, а дальше копирует ходы игрока"""

        def add_candy(candy_, match, flags):
            if flags["match_c_c"] == 0:
                n = list(Players.Cooperator.add_candy(candy_))
                if candy_ != 2:
                    flags["flags1"] = 1
                    candy = 0
            if flags["match_c_c"] == 0:
                flags["match_c_c"] = 1
                return n[0], candy_
            candy = int(candy_)
            score = 0
            sum_p_p = int(flags["candy_p1"]) + int(flags["candy_p2"])
            if candy == 2 and sum_p_p == 4:
                score = 2
                if match == 8:
                    candy = 0
                return score, candy
            elif candy == 2 and sum_p_p == 2:
                score = 3
                if match == 8:
                    candy = 0
                return score, candy
            elif candy == 0 and sum_p_p == 2:
                score = -1
                if match == 8:
                    candy = 0
                return score, candy
            candy = 0
            return score, candy

    class Gradger(object):
        """Начинает как кооператор, но если игрок сделал чит, то становится читером"""

        def add_candy(candy_, match, flags):
            candy = candy_
            if candy_ != 2:
                candy = 0
            if match == 0:
                n = list(Players.Cooperator.add_candy(candy))
                if candy_ != 2:
                    flags["flags1"] = 1
                    candy = 0
                return n[0], candy
            if flags["flags1"] == 0:
                if candy_ != 2:
                    flags["flags1"] = 1
                    candy = 0
                n = list(Players.Cooperator.add_candy(candy))
                return n[0], candy

            return list(Players.Cheater.add_candy(candy))

    class Detectitve(object):
        """1 - кооператор, 2 - чит, 3 и 4 -кооператор,
        Ecли был 1 чит в течении 4-x, то становится copycat
        Иначе становится cheat"""

        def add_candy(candy, match, flags):
            if match == 0 or match == 1 or match == 2 or match == 3:
                if candy != 2:
                    flags["flags2"] = 1
            if match == 0:
                n = list(Players.Cooperator.add_candy(candy))
                return n[0], 0
            # poунд2
            if match == 1:
                n = list(Players.Cheater.add_candy(candy))
                return n[0], 2
            # poунд3
            if match == 2:
                n = list(Players.Cooperator.add_candy(candy))
                return n[0], 2
            # poунд4
            if match == 3:
                n = list(Players.CopyCat.add_candy(candy, flags))
                if flags["flags2"] == 0:
                    candy = 0
                return n[0], candy
            if flags["flags2"] == 0:
                return list(Players.Cheater.add_candy(candy))
            return list(Players.CopyCat.add_candy(candy, flags))

    class My(object):
        """Всегда 1"""

        def add_candy(candy, flags):
            score = 0
            sum_p_p = int(flags["candy_p1"]) + int(flags["candy_p2"])
            if candy == 2 and sum_p_p == 4:
                score = 2
            elif candy == 2 and sum_p_p == 2:
                score = 3
            elif candy == 0 and sum_p_p == 2:
                score = -1
            return score, candy


class Start(object):
    def starts():
        print("\033c", end="")
        print("\t\t\t*****************************************")
        print("\t\t\t*  Выбери кто будет играть через пробел *")
        print("\t\t\t*****************************************")
        print("\t\t\tЦифрами от 1 до 7")
        print(
            "\t\t\t1- cheater (всегда лжет)\n\t\t\t2-cooperator (всегда дает)"
        )
        print("\t\t\t3-copycat(1-й раз дает, а потом копирует игрока)")
        print(
            "\t\t\t4-granger (дает, но если соперник зажал, то становится cheater)"
        )
        print(
            "\t\t\t5-detectiv(1 - кооператор, 2 - чит, 3 и 4 -кооператор, еcли был 1 чит в течении 4-x,\n\t\t\t то становится copycat, иначе становится cheat)"
        )
        print(
            "\t\t\t6-my(как copy cat, но последнюю никогда не даст)\n\t\t\t7-you version(сам выбираешь)"
        )
        text = input()

        num = [0] * 7
        for i in range(7):
            if text.count(str(i + 1)):
                num[i] = int(i + 1)

        print("\033c", end="")
        print("ты выбрал", num)
        sleep(2)
        return num


if __name__ == "__main__":
    t = (1, 2, 3, 4, 5)
    n = Game(10, t)
    n.play()
    n.top3()
    t = (1, 2, 3, 4, 5, 6)
    n = Game(10, t)
    n.play()
    print("\n")
    n.top3()

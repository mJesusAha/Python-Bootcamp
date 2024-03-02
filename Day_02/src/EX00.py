# python3 EX00.py
class MyKey:
    """В этом классе что то про пароль"""

    def __init__(
        self,
        password,
    ):
        self.password = password
        self._passphrase = password

    @property
    def passphrase(self):
        if self._passphrase != "zax2rulez":
            print('AssertionError: key.passphrase == "zax2rulez"')
        return self._passphrase

    def __len__(self):
        if self.password.count("zax") or len(self.password) == 1337:
            return 1337
        print("AssertionError: key == 1337")
        return len(self.password)

    def __getitem__(self, arg):
        if arg == 404 and self.password.count("2"):
            return 3
        elif 0 <= len(self.password) - 1 <= arg:
            print("AssertionError: key[404] == 3")
            return self.password[len(self.password) - 1]
        print("AssertionError: key[404] == 3")
        return None

    def __str__(self) -> str:
        if (
            self.password == "zax2rulez"
            or str(self.password) == "GeneralTsoKeycard"
        ):
            return "GeneralTsoKeycard"
        print('AssertionError: str(key) == "GeneralTsoKeycard"')
        return str(self.password)

    def __gt__(self, __o: object) -> bool:
        if self.password.count("rulez"):
            return True
        if self.password.isdigit() == True and int(self.password) > 9000:
            return True
        print("AssertionError: key > 9000")
        return len(self.password) > (__o)


if __name__ == "__main__":
    key: MyKey
    print("При не правильном вводе")
    key = MyKey("1")
    len(key)
    key[404]
    key.passphrase
    str(key)
    key > 9000
    print("При правильном вводе нет ошибок")
    key = MyKey("zax2rulez")
    len(key)
    key[404]
    key.passphrase
    str(key)
    key > 9000
    print("При правильном вводе проверка")
    print(len(key))
    print(key[404])
    print(key.passphrase)
    print(str(key))
    print(key > 9000)

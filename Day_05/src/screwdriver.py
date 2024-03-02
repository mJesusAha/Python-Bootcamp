# python3 screwdriver.py load /Users/mv/Desktop/melody/sample-3s.wav    после load адрес
# python3 screwdriver.py list   выведет список

import sys
import os

if len(sys.argv) > 1:
    if sys.argv[1] == "load" and len(sys.argv) >= 3:
        load = str(sys.argv[1])
        address = str(sys.argv[2])
        os.system(f"curl -X POST -F 'file=@'{address}'' 127.0.0.1:8888/success")

    elif sys.argv[1] == "list":
        print("\t\033[34mсписок")
        os.system(f"curl '127.0.0.1:8888/?playlist=playlist'")
        print("\n")
    else:
        print(
            "\033[33mОшибка запроса\n load адрес - для загрузки файлов\n list покажет список "
        )
else:
    print(
        "\033[33mОшибка запроса\n load адрес - для загрузки файлов\n list покажет список "
    )

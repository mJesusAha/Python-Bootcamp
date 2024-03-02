# EX02
# python3 produser.py
import json
import random
import redis
import logging
import time


def gen_int2():
    number_str = 0
    while number_str == 0:
        number_str = random.randint(-9, 9)
    int_str = str(number_str) + "000"
    return int(int_str)


def gen_int():
    number_str = random.randint(1, 9)
    int_str = str(number_str) * 10
    return int(int_str)


counter = 0
redis_client = redis.Redis(host="localhost", port=6379, db=0)
while counter != 10:
    n1 = gen_int()
    n2 = gen_int()
    n3 = gen_int2()
    dict_metadata = {"metadata": {"from": n1, "to": n2}, "amount": n3}
    if n1 != n2:
        # Для бесконечности закоментируй строку ниже////
        counter+=1                                   #//
        # //////////////////////////////////////////////
        message = json.dumps(dict_metadata)
        redis_client.publish("channel_1", message)

        print(message)
        logging.info(message)
        time.sleep(0.1)
redis_client.close()

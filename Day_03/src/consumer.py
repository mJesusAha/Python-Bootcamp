# EX02
# python3 consumer.py -e 1111111111 7777777777 8888888888
import redis
import time
import json
import logging
from sys import argv


def new_str(argv, message):
    dict_metadata = ""
    t = str(message)
    t = t[73:-2]
    dict_t = "{" + t
    if len(dict_t) >= 68:
        n = json.loads(dict_t)
        from_to = n["metadata"]
        n_to = from_to["to"]
        n_from = from_to["from"]
        if n["amount"] > 0:
            argv_str = str(argv)
            if len(argv) > 1 and argv[1] == "-e" and argv_str.count(str(n_to)):
                n_to = from_to["from"]
                n_from = from_to["to"]
        dict_metadata = {
            "metadata": {"from": n_from, "to": n_to},
            "amount": n["amount"],
        }
    return dict_metadata


r = redis.Redis(host="localhost", port=6379, db=0)
logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
p = r.pubsub()
p.subscribe("channel_1", "metadata")
t = 0
while True:
    message = p.get_message()
    # Для бесконечности закоментируй строку ниже////
    if t == 10: break                          #//
    # //////////////////////////////////////////////

    if len(str(message)) > 80:
        t = t + 1
        dict_str = new_str(argv, message)

        logger.info(dict_str)
        time.sleep(0.01)
        r.close()

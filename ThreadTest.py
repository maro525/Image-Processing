from logging import (getLogger, StreamHandler, INFO, Formatter)

# ログの設定
handler = StreamHandler()
handler.setLevel(INFO)
handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
logger = getLogger()
logger.addHandler(handler)
logger.setLevel(INFO)


from threading import (Event, Thread)
import time

event = Event()

# example 1
# https://qiita.com/tag1216/items/2dcb112f8018eb19a999
# def event_example1():
#     logger.info("スレッド開始")
#     event.wait()
#     logger.info("スレッド終了")
#
# thread = Thread(target=event_example1)
# thread.start()
# time.sleep(3)
# logger.info("イベント発生")
# event.set()


# example 3
stop = False # イベント停止のフラグ

def event_example3():
    logger.info("スレッド開始")
    count = 0
    while not stop:
        logger.info("event wait")
        event.wait()
        logger.info("event clear")
        event.clear()
        logger.info(count)
        count += 1
        logger.info(count)
    logger.info("スレッド終了")

thread = Thread(target=event_example3)
thread.start()

time.sleep(1)
logger.info("sleep finish")
event.set()
logger.info("event set")
time.sleep(1)
logger.info("sleep finish")
event.set()
logger.info('event set')
time.sleep(1)
logger.info("sleep finish")
stop = True
logger.info("boolean flipped")
event.set()
logger.info("event set")


thread.join()

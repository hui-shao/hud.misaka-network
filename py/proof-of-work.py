import hashlib
import random
import threading
import time
import queue


class Hashrate:
    def __init__(self):
        self.active = True
        self.time = time.time()

    def stop(self):
        self.active = False

    def show_current_hashrate(self):
        while self.active:
            if not timer1_queue.empty():
                y = timer1_queue.get()
                timer1_queue.queue.clear()
                duration = 5
                time.sleep(duration)
                m, s = divmod(time.time() - self.time, 60)
                h, m = divmod(m, 60)
                print("SHA256 - Speed:" + str((int(timer1_queue.get()) - y) / duration)
                      + "H/s, 摸鱼时间:" + "%02d:%02d:%02d" % (h, m, s))
        return 0


print("猛男: Generating Puzzle")

puzzle = random.randint(0, 100000000000)

zero_prefix = 6

print("猛男: Puzzle - find a string or number that ends with " + str(puzzle)
      + " and its sha256 starts with " + "0" * zero_prefix)

data_sent_puzzle = str(puzzle)

data_sent_zero_prefix = zero_prefix

print("秦川: Working on it...")

i = 0
timer1_queue = queue.Queue()
timer1 = Hashrate()
timer1_thread = threading.Thread(target=Hashrate.show_current_hashrate, args=(timer1,))
timer1_thread.start()
while True:
    timer1_queue.put(i)
    if str(hashlib.sha256((str(i) + data_sent_puzzle).encode("utf-8")).hexdigest())[0:data_sent_zero_prefix]\
            == "0" * data_sent_zero_prefix:
        print("秦川: 我摸到啦！")
        print("秦川: Solution  " + str(i) + str(data_sent_puzzle))
        print("秦川: SHA256    " + hashlib.sha256((str(i) + data_sent_puzzle).encode("utf-8")).hexdigest())
        break
    i += 1

data_return_str = str(i) + str(data_sent_puzzle)
timer1.stop()
print("猛男: Auth...")

if str(hashlib.sha256(data_return_str.encode("utf-8")).hexdigest())[0:zero_prefix] == "0" * zero_prefix:
    print("猛男: 似李！缺！")
    print("猛男: Received  " + data_return_str)
    print("猛男: SHA256    " + str(hashlib.sha256(data_return_str.encode("utf-8")).hexdigest()))
else:
    print("猛男: 秦川一样的返回值")
    print("猛男: Received  " + data_return_str)
    print("猛男: SHA256    " + str(hashlib.sha256(data_return_str.encode("utf-8")).hexdigest()))

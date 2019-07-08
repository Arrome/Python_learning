__author__ = 'Arrome'

import sys
import time
# d=0
# for data in range(1,11):
#     time.sleep(0.2)
#     d += 1
#     done = int(50* d / 10)
#     sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done),10*d))
#     sys.stdout.flush()


def processbar(done, total):
    done = int(50* done/total)
    sys.stdout.write("\r[%s%s] %d%%" % ('=' * done, '-' * (50 - done),2* done))
    sys.stdout.flush()

if __name__ == "__main__":
    for i in range(1,101):
        time.sleep(0.2)
        processbar(i,100)
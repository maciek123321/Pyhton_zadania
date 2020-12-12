import threading
import time
from numpy import random


def hist(histo, array):
    for m in array:
        histo[m] += 1


if __name__ == '__main__':

        a = 10
        histo = []
        for i in range(a):
            histo.append(0)

        array = x=random.randint(a, size=(100000))
        start = time.perf_counter()

        p1 = threading.Thread(target=hist(histo, array[0:int(100000/4)]))
        p2 = threading.Thread(target=hist(histo, array[int(100000/4):int(100000/2)]))
        p3 = threading.Thread(target=hist(histo, array[int(100000/2):int((100000/4)*3)]))
        p4 = threading.Thread(target=hist(histo, array[int((100000/4)*3):100000]))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        stop = time.perf_counter() - start

        print(histo)
        print(stop)


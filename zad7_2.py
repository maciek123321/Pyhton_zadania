import threading
import random
import time


class Philosopher(threading.Thread):
    running = True

    def __init__(self, xname, Left, Right):
        threading.Thread.__init__(self)
        self.name = xname
        self.Left = Left
        self.Right = Right

    def run(self):
        while (self.running):
            time.sleep(random.uniform(3, 13))
            print('%s is hungry' % self.name)
            self.dine()

    def dine(self):
        fork1, fork2 = self.Left, self.Right

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print('%s swaps forks' % self.name)
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print('%s Eating...' % self.name)
        time.sleep(random.uniform(1, 3))
        print('%s Thinking...' % self.name)


def DiningPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    names = ('Schopenhauer', 'Nietzsche', 'Engels', 'Marx', 'Kant')

    philosophers = [Philosopher(names[i], forks[i % 5], forks[(i + 1) % 5]) \
                    for i in range(5)]
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(20)
    Philosopher.running = False


if __name__ == '__main__':

    DiningPhilosophers()

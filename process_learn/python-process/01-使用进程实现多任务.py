import multiprocessing
import time


def test1():
    while True:
        print("1--------")
        time.sleep(1)


def test3():
    while True:
        print("3--------")
        time.sleep(1)


def test2():
    p1 = multiprocessing.Process(target=test3)
    p1.start()
    while True:
        print("2--------")
        time.sleep(1)


def main():
    #    t1 = threading.Thread(target=test1)
    #    t2 = threading.Thread(target=test2)
    #    t1.start()
    #    t2.start()

    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()

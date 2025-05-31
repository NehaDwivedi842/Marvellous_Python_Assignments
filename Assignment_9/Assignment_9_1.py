import threading
import time

def thread1():
    print("Thread 1 is running")
    for i in range(1,6):
        print(i)
    time.sleep(1)

def thread2():
    print("Thread 2 is running")
    for i in range(1,6):
        print(i)
    time.sleep(1)

def thread3():
    print("Thread 3 is running")
    for i in range(1,6):
        print(i)
    time.sleep(1)

def main():
    T1 = threading.Thread(target=thread1)
    T2 = threading.Thread(target=thread2)
    T3 = threading.Thread(target=thread3)

    T1.start()
    T1.join()
    T2.start()
    T2.join()
    T3.start()
    T3.join()


if __name__ == "__main__":
    main()


import threading

def Thread1():
    print("Thread 1 is running")
    for i in range(1, 51):
        print(i)

def Thread2():
    print("Thread 2 is running")
    for i in range(50, 0,-1):
        print(i)

def main():
    T1=threading.Thread(target=Thread1)
    T2=threading.Thread(target=Thread2)
    T1.start()
    T1.join()
    T2.start()
    T2.join()   
   
if __name__=="__main__":
    main()
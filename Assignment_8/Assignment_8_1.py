import threading

def DisplayEven():
    print("First 10 Even Numbers:")
    for i in range(1,21):
        if i%2==0:
            print(i)

def DisplayOdd():
    print("First 10 Odd Numbers:")
    for i in range(1,21):
        if i%2!=0:
            print(i)

def main():
    T1=threading.Thread(target=DisplayEven)
    T1.start()
    T1.join()
    T2=threading.Thread(target=DisplayOdd)
    T2.start()
    T2.join()
   
   
if __name__=="__main__":
    main()
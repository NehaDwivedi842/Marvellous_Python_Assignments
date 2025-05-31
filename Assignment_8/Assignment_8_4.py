import threading

def Capital(A):
    count = 0
    for i in range(len(A)):
        if A[i].isupper():
            count += 1
    print("Number of Capital Letters:", count)
    print("Thread Id and Name:", threading.get_ident(), threading.current_thread().name)

def Small(A):
    count = 0
    for i in range(len(A)):
        if A[i].islower():
            count += 1
    print("Number of Small Letters:", count)
    print("Thread Id and Name:", threading.get_ident(), threading.current_thread().name)

def Digit(A):
    count = 0
    for i in range(len(A)):
        if A[i].isdigit():
            count += 1
    print("Number of Digit Letters:", count)
    print("Thread Id and Name:", threading.get_ident(), threading.current_thread().name)


def main():
    text=input("Enter a string:")

    T1=threading.Thread(target= Capital,args=(text,))
    T2=threading.Thread(target= Small,args=(text,))
    T3=threading.Thread(target=Digit,args=(text,))
    T1.start()
    T2.start()
    T3.start()
    T1.join()
    T2.join()
    T3.join()
    print("Exit from main")
   
   
if __name__=="__main__":
    main()
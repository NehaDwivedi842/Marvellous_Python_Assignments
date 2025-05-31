import threading

def EvenFactor(A):
    print ("Even Factors:")
    for i in range(1,A+1):
        if A%i==0:
            if i%2==0:
                print(i)

def OddFactor(B):
    print ("Odd Factors:")
    for i in range(1,B+1):
        if B%i==0:
            if i%2!=0:
                print(i)

def main():
    num = int(input("Enter a number to find its even and odd factors:"))
    T1=threading.Thread(target=EvenFactor,args=(num,))
    T2=threading.Thread(target=OddFactor,args=(num,))
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    print("Exit from main")
   
   
if __name__=="__main__":
    main()
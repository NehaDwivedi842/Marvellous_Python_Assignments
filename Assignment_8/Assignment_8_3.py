import threading

def EvenList(A):
    sum=0
    for i in A:
         if i%2==0:
            sum+=i
    print("Sum of Even Numbers:", sum)

def OddList(B):
    sum=0
    for i in B:
        if i%2!=0:
            sum+=i
    print("Sum of Odd Numbers:", sum)

def main():
    num = int(input("Enter how many numbers you want to input: "))
    data = []

    for i in range(num):
        val = int(input(f"Enter number:"))
        data.append(val)


    T1=threading.Thread(target=EvenList,args=(data,))
    T2=threading.Thread(target=OddList,args=(data,))
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    print("Exit from main")
   
   
if __name__=="__main__":
    main()
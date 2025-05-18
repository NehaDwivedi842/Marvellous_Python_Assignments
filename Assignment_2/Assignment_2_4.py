

def main():
    No1=int(input("Enter Number:"))
    sum=0
    for i in range(1,No1,1):
        if No1%i==0:
            sum=sum+i
        i=i-1
    print("Sum of Factors is:",sum)
    


if __name__=="__main__":
    main()
#returns sum of digit in number

def main():
    No=int(input("Enter Number:"))
    sum=0
    while(No!=0):
        sum=sum+(No%10)
        No=No//10
    print("Sum of Digit is:",sum)

if __name__=="__main__":
    main()
def main():
    no=int(input("Enter the Number:"))
    prime=True
    
    if no>1:
        for i in range(2,no):
            if no%i==0:
                prime=False
                break
        if prime:
            print(no,"is a Prime Number")
        else:
            print(no,"is not a Prime Number")
    else:
        print(no,"is not a Prime Number")
        
    
if  __name__== "__main__":
    main()
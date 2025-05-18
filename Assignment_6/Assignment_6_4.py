def main():
    no=int(input("Enter the Number:"))
    Factorial=1
    for i in range(no,0,-1):
        Factorial=Factorial*i
    print("Factorial of",no,"is:",Factorial)
        
    
if  __name__== "__main__":
    main()
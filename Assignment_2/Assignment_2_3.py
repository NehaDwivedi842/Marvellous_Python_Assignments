def main():
    No1=int(input("Enter Number:"))
    Factorial=1
    for i in range(No1,0,-1):
        Factorial=Factorial*i
        i=i-1
    print("Factorial is:",Factorial)

if __name__=="__main__":    
    main()
    
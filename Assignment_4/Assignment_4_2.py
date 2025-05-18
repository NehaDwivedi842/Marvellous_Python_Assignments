def main():
    no1=int(input("Enter First no:"))
    no2=int(input("Enter Second no:"))

    Mult=lambda X,Y:X*Y

    result=Mult(no1,no2)
    print("Result is:",result)

if __name__== "__main__":
    main()

    
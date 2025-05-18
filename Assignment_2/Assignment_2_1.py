from Arithmetic import Add,Sub,Mult,Div

def main():
    Value1=int(input("Enter First Number for Addition:"))
    Value2=int(input("Enter Second Number for Addition:"))
    print("Addition is:",Add(Value1,Value2))

    Value3=int(input("Enter First Number for Subtraction:"))
    Value4=int(input("Enter Second Number for Subtraction:"))
    print("Substraction is:",Sub(Value3,Value4))

    Value5=int(input("Enter First Number for Multiplication:"))
    Value6=int(input("Enter Second Number for Multiplication:"))
    print("Multiplication is:",Mult(Value5,Value6))

    Value7=int(input("Enter First Number for Division:"))
    Value8=int(input("Enter Second Number for Division:"))
    print("Division is:",Div(Value7,Value8))

if __name__=="__main__":
    main()
def ChkNum(no):
    if no%2==0:
        print("Even Number")
    else:
        print("Odd Number")


def main():
    print("Enter Number:")
    Value=int(input())
    ChkNum(Value)

if __name__=="__main__":
    main()
def CheckDivisibility(no1):
    if no1%5==0:
        return True
    else:
        return False
    
def main():
    print("Enter the number:")
    Value=int(input())
    result=CheckDivisibility(Value)
    print(result)

if __name__=="__main__":
    main()
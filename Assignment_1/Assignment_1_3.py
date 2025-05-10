def Add(Value1,Value2):
    ans=Value1+Value2
    return ans

def main():
    print("Enter First number:")
    no1=int(input())
    print("Enter Second number:")
    no2=int(input())
    result=Add(no1,no2)
    print("Addition is:",result)

if __name__=="__main__":
    main()

def prime(value):
    if value<=1:
        return False
    for i in range(2,value):
        if value%i==0:
            return False
    return True 
def main():
    no=int(input("Enter number of elements: "))
    data=[]
    print("Enter elements:")
    for i in range(no):
        no1=int(input())
        data.append(no1)
    print("Data:",data)

    result=list(filter(prime,data))
    
    print("Prime Numbers:",result)

if  __name__=="__main__":
    main()
def Even(x):
    if x%2==0:
        return True
    else:
        return False

def main():
    no=int(input("Enter number of elements: "))
    data=[]
    print("Enter elements:")
    for i in range(no):
        no1=int(input())
        data.append(no1)
    print("Data:",data)

    result=list(filter(Even,data))
    
    print("Even Numbers:",result)

if  __name__=="__main__":
    main()
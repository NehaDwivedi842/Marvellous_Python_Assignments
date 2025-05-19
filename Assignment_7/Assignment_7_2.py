def double(x):
    return x*2

def main():
    no=int(input("Enter number of elements: "))
    data=[]
    print("Enter elements:")
    for i in range(no):
        no1=int(input())
        data.append(no1)
    print("Data:",data)

    result=list(map(double,data))
    print("Double List:",result)

if  __name__=="__main__":
    main()
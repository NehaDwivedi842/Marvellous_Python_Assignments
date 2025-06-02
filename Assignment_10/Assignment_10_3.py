from functools import reduce

Greater=lambda X:X>=70 and X<=90
Increase=lambda Y:Y+10
Product=lambda X,Y:X*Y

def main():
    data=[]

    no=int(input("Enter no of elements in list: "))

    for i in range(no):
        val=int(input("Enter value: "))
        data.append(val)

    print("Input Data:",data)

    FData=list(filter(Greater,data))
    print("Filter Data : ",FData)
    
    MData=list(map(Increase,FData))
    print("Map Data : ",MData)

    RData=int(reduce(Product,MData))
    print("Reduce Data : ",RData)


if __name__=="__main__":
    main()




from functools import reduce

Even=lambda X:X%2==0
Square=lambda Y:Y**2
Sum=lambda X,Y:X+Y

def main():
    data=[]

    no=int(input("Enter no of elements in list: "))

    for i in range(no):
        val=int(input("Enter value: "))
        data.append(val)

    print("Input Data:",data)

    FData=list(filter(Even,data))
    print("Filter Data : ",FData)
    
    MData=list(map(Square,FData))
    print("Map Data : ",MData)

    RData=int(reduce(Sum,MData))
    print("Reduce Data : ",RData)


if __name__=="__main__":
    main()




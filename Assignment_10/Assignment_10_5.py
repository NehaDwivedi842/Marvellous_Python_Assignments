from functools import reduce

def Prime(X):
    for i in range(2,X):
        if X%i==0:
            return False
    else:
        return True

def Multiply(X):
    return X*2

def Maximum(X,Y):
    if X>Y:
        return X
    else:
        return Y



def main():
    data=[]

    no=int(input("Enter no of elements in list: "))

    for i in range(no):
        val=int(input("Enter value: "))
        data.append(val)

    print("Input Data:",data)

    FData=list(filter(Prime,data))
    print("Filter Data : ",FData)
    
    MData=list(map(Multiply,FData))
    print("Map Data : ",MData)

    RData=int(reduce(Maximum,MData))
    print("Reduce Data : ",RData)


if __name__=="__main__":
    main()




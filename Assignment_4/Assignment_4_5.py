from functools import reduce
def Filterout(no):
    if no ==1:
        return None
    for i in range(2, no):
        if no % i == 0:
            return None
    return no

def Mapout(data):
     return data*2

def Max(A, B):
    return A if A > B else B
     
def main():
    no = int(input("Enter Number of Elements: "))
    data = []
    print("Enter Elements:")
    for i in range(no):
        num = int(input())
        data.append(num)
        
    print("Input Data : ",data)
    Fdata=list(filter(Filterout,data))
    print(Fdata)
    Mdata=list(map(Mapout,Fdata))
    print(Mdata)
    Rdata=int(reduce(Max,Mdata))
    print(Rdata)

if __name__=="__main__":
    main()
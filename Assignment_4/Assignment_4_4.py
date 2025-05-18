from functools import reduce
def Filterout(data):
     if data%2==0:
        return data

def Mapout(data):
     return data**2

def Product(A,B):
     return A+B
     

def main():
    data=[5,2,3,4,3,4,1,2,8,10]
    print("Input Data : ",data)
    Fdata=list(filter(Filterout,data))
    print(Fdata)
    Mdata=list(map(Mapout,Fdata))
    print(Mdata)
    Rdata=int(reduce(Product,Mdata))
    print(Rdata)

if __name__=="__main__":
    main()
from functools import reduce
def Filterout(data):
     if data >= 70 and data <= 90:
            return data

def Mapout(data):
     return data+10

def Product(A,B):
     return A*B
     


def main():
    data=[4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    print("Input Data : ",data)
    Fdata=list(filter(Filterout,data))
    print(Fdata)
    Mdata=list(map(Mapout,Fdata))
    print(Mdata)
    Rdata=int(reduce(Product,Mdata))
    print(Rdata)

if __name__=="__main__":
    main()
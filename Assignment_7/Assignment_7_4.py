from functools import reduce
def product (x,y):
    return x*y

def main():
    no=int(input("Enter number of elements: "))
    data=[]
    print("Enter elements:")
    for i in range(no):
        no1=int(input())
        data.append(no1)
    print("Data:",data)

    result=reduce(product,data)
    print("Product:",result)

if  __name__=="__main__":
    main()
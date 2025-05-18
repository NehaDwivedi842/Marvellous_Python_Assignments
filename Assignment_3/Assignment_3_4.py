def Frequency(data,val):
    count=0
    for j in data:
        if j == val:
            count=count+1
    print("Frequency of Number is :",count)

def main():
    no=int(input("Enter Number of Elements:"))
    data=[]
    print("Enter Elements:")
    for i in range(no):
        i=int(input())
        data.append(i)
    print(data)
    val=int(input("Enter the value to find frequency:"))
    Frequency(data,val)
    

if __name__=="__main__":
    main()
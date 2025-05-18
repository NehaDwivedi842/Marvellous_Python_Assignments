def addition(data):
        sum=0
        for j in data:
            sum=sum+j
        print(sum)

def main():
    no=int(input("Enter Number of Elements:"))
    data=[]
    print("Enter Elements:")
    for i in range(no):
        i=int(input())
        data.append(i)
    print(data)
    addition(data)

if __name__=="__main__":
    main()
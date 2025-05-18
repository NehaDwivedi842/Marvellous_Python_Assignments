def Max(data):
        maximum=data[0]
        for j in data:
            if j > maximum:
                 maximum=j
        print("Maximum Number is :",maximum)

def main():
    no=int(input("Enter Number of Elements:"))
    data=[]
    print("Enter Elements:")
    for i in range(no):
        i=int(input())
        data.append(i)
    print(data)
    Max(data)

if __name__=="__main__":
    main()
def Min(data):
        minimum=data[0]
        for j in data:
            if j < minimum:
                 minimum=j
        print("Minumum Number is :",minimum)

def main():
    no=int(input("Enter Number of Elements:"))
    data=[]
    print("Enter Elements:")
    for i in range(no):
        i=int(input())
        data.append(i)
    print(data)
    Min(data)

if __name__=="__main__":
    main()
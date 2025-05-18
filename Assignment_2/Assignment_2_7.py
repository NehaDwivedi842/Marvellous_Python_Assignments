def main():
    No=int(input("Enter Number:"))
    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j,end=" ")
        print()
        i=i+1

if __name__=="__main__":
    main()
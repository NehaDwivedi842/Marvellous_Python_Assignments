
def main():
    No=int(input("Enter Number:"))
    i=0
    while(No!=0):
        No=No//10
        i=i+1
    print(i)

if __name__=="__main__":
    main()
def Prime(No):
    for i in range(2,No):
        if No%i==0:
            return False
    return True

def main():
    No=int(input("Enter Number:"))
    if Prime(No):
        print("Prime Number")
    else:
        print("Not Prime Number")

if __name__=="__main__":
    main()
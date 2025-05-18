
# print largest number from five numbers

def main():
    print("Enter five Number:")
    no1=int(input())
    no2=int(input())
    no3=int(input())
    no4=int(input())
    no5=int(input())

    if no1>no2 and no1>no3 and no1>no4 and no1>no5:
        print("Largest number is:",no1)
    elif no2>no1 and no2>no3 and no2>no4 and no2>no5:
        print("Largest number is:",no2)
    elif no3>no1 and no3>no2 and no3>no4 and no3>no5:
        print("Largest number is:",no3) 
    elif no4>no1 and no4>no2 and no4>no3 and no4>no5:
        print("Largest number is:",no4)
    else:
        print("Largest number is:",no5)

if  __name__== "__main__":
    main()

        

    
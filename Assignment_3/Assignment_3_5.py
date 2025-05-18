from MarvellousNum import ChkPrime
from MarvellousNum import ChkPrime

def ListPrime():
    no = int(input("Enter Number of Elements: "))
    data = []
    print("Enter Elements:")
    for i in range(no):
        num = int(input())
        data.append(num)
    
    total = 0
    for value in data:
        if ChkPrime(value)== True:
            total += value

    print("Sum of Prime Numbers is:", total)

def main():
    ListPrime()

if __name__=="__main__":
    main()
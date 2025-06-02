sum = 0

def sum_digits(n):
    global sum
    if n == 0:
        return
    sum += n % 10
    sum_digits(n // 10)
    return sum

def main():
    global sum  
    sum = 0
    n = 1234
    result = sum_digits(n)
    print(f"The sum of digits is: {result}")

if __name__ == "__main__":
    main()

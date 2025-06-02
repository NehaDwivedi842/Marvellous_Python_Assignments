
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
    
def main():
    x = 2
    n = 3
    result = power(x, n)
    print(result)

if __name__ == "__main__":
    main()
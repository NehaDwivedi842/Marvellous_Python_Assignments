# sum of n natural numbers using recursion and global variable

sum = 0

def sum_n(n):
    global sum
    if n == 0:
        return
    sum += n
    sum_n(n - 1)
    return sum

def main():
    n = 5
    result = sum_n(n)
    print(f"The sum of natural numbers is: ", result)

if __name__ == "__main__":
    main()

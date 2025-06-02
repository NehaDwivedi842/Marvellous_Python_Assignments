# count zerosin number recursively using global

count = 0
def count_zeros(n):
    global count
    if n == 0:
        return
    if n % 10 == 0:
        count += 1
    count_zeros(n // 10)

def main():
    n = 1020300
    count_zeros(n)
    print(f"The number of zeros in is:", count)

if __name__ == "__main__":
    main()
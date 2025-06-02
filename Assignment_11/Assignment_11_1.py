# recursive function to print numbers from 0 to N
ret=0
def numbers(n):
    if n == 0:
        return
    numbers(n - 1)
    print(n, end=' ')


def main():
    n = 5
    numbers(n)

if __name__ == "__main__":
    main()

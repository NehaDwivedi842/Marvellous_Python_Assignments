p=''

def display(n):
    global p
    if n == 0:
        return
    display(n - 1)
    p += '* ' * n + '\n'
    

def main():
    n = 4
    display(n)
    print(p, end='')

if __name__ == "__main__":
    main()


factorial=1
def fact(no):
    global factorial
    if (no>=1):
        factorial=factorial* no
        no=no-1
        fact(no)
    return factorial

def main():
    Ret=fact(5)
    print(Ret)

if __name__=="__main__":
    main()

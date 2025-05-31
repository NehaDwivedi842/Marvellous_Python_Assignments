import multiprocess
import multiprocess.pool

def factorial(x):
    val=1
    for i in range(1, x+1):
        val=val*i
    return val

def main():
    data = [5,6,7,4]
    P1 = multiprocess.Pool()
    ans=P1.map(factorial, data)
    print("Factorial of numbers:", ans)



if __name__ == "__main__":
    main()



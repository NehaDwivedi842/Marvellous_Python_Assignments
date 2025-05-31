import multiprocess

def square(x):
    result=[]
    for i in x:
        result.append(i * i)
    print(result)

def main():
    data = [1, 2, 3, 4, 5,13,11]
    P1 = multiprocess.Process(target=square, args=(data,))
    P1.start()
    P1.join()


if __name__ == "__main__":
    main()



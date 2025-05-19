Square=lambda X: X**2

Cube=lambda X : X**3

def main():
    no=int(input("Enter a number: "))
    sqr=Square(no)
    cub=Cube(no)
    print("Square:",sqr)
    print("Cube:",cub)

if __name__=="__main__":
    main()
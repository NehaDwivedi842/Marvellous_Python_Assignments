def main():
    a=input("Enter a string: ")
    if a[::-1]==a:
        print("String is Pallindrome")
    else:
        print("String is not Pallindrome")
        

if __name__=="__main__":
    main()
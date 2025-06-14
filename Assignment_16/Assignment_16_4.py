import os

def main():
        fobj=open("number.txt","w")
        for i in range (10):
            no=int(input("Enter numbers:"))
            fobj.write(str(no)+"\n")
            i=i+1
        fobj.close()
   
if __name__=="__main__":
    main() 
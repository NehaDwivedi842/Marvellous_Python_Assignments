import os

def main():
    if os.path.exists("Data.txt"):
        fobj=open("Data.txt","r")
        data=fobj.read()
        print("Content from file is:\n",data)
        fobj.close()
    else:
        print("Data.txt File does not exists.")

if __name__=="__main__":
    main() 
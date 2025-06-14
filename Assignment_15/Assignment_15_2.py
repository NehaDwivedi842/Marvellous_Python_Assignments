import os

def main():
    file_name=input("Enter file name which you want to display:")

    if os.path.exists(file_name):
        fobj=open(file_name,"r")
        data=fobj.read()
        print("Data from file is:\n",data)
        fobj.close()
    else:
        print("File does not exists.")

if __name__=="__main__":
    main() 
import os
import sys

def main():
    if (len(sys.argv)==2):
        file_name=sys.argv[1]

        if os.path.exists(file_name):
            newfile=open("Demo.txt","w")
            fobj=open(file_name,"r")
            data=fobj.read()
            newfile.write(data)
            fobj.close()
            newfile.close()
        else:
            print("File does not exists.")
    else:
        print("Use the given script as : python ScriptName.py file_name")
        print("file_name is the name of file which you want to copy")

if __name__=="__main__":
    main() 
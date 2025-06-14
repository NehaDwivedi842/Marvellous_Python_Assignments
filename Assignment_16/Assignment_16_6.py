import os
import sys

def main():
    if os.path.exists("Source.txt"):
        newfile=open("Destination.txt","w")
        fobj=open("Source.txt","r")
        data=fobj.read()
        newfile.write(data)
        fobj.close()
        newfile.close()
    else:
        print("File does not exists.")
    
if __name__=="__main__":
    main() 
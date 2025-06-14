import os
import sys

def main():
    if (len(sys.argv)==3):
        file_name1=sys.argv[1]
        file_name2=sys.argv[2]


        if os.path.exists(file_name1) and os.path.exists(file_name2) :
            newfile=open(file_name1,"r")
            fobj=open(file_name2,"r")
            data1=fobj.read()
            data2=newfile.read()
            if data1==data2:
                print("Sucess")
            else:
                print("Comparison failed. Content not same")
            newfile.close()
            fobj.close()
        else:
            print("File does not exists.")
    else:
        print("Use the given script as : python ScriptName.py file_name1 file_name2")
        print("file_names are the name of files which you want to compare")

if __name__=="__main__":
    main()
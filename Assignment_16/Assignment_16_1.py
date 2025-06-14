import os

def main():
        fobj=open("student.txt","w")
        for i in range (5):
            s_name=input("Enter name of students:")
            fobj.write(s_name+"\n")
            i=i+1
        fobj.close()
   

if __name__=="__main__":
    main() 
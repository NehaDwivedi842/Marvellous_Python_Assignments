import os

def main():
    file_name=input("Enter file name:")

    if os.path.exists(file_name):
        print("File already exists.")
    else:
        print("File does not exists.")

if __name__=="__main__":
    main() 
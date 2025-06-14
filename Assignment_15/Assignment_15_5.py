import os


def main():
    file_name = input("Enter the file name: ")         
    search_str = input("Enter the string to search: ")

    if os.path.exists(file_name):
         with open(file_name, 'r') as file:
              content=file.read()
              count=content.count(search_str)
              print(f"The word frquency is:",count)


if __name__=="__main__":
    main()
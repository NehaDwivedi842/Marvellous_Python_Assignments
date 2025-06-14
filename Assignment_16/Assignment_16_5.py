import os

def main():
    if os.path.exists("fiveline.txt"):
        with open("fiveline.txt", "r") as file:
            for line in file:
                words = line.split()
                if len(words) > 5:
                    print(line.strip())
    else:
        print("Data.txt file does not exist.")

if __name__ == "__main__":
    main()
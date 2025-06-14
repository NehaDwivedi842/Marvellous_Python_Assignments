def main():
    with open("marks.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                name, marks = parts[0], int(parts[1])
                if marks > 75:
                    print(f"{name} scored {marks}")

if __name__=="__main__":
    main() 
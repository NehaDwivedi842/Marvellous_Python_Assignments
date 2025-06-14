def main():
    try:
        with open("Data.txt", 'r') as file:
            content = file.read()

            lines = content.splitlines()
            words = content.split()
            chars = len(content)

            print(f"Lines: {len(lines)}")
            print(f"Words: {len(words)}")
            print(f"Characters: {chars}")

    except FileNotFoundError:
        print("Data.txt file does not exist.")

if __name__ == "__main__":
    main()

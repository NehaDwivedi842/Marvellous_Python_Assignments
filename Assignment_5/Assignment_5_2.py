def main():
    word=input("Enter a character:")

    if word in ['a','e','i','o','u','A','E','I','O','U']:
        print(word + " is a vowel")

    else:
        print(word + " is a consonant")
    
if  __name__== "__main__":
    main()

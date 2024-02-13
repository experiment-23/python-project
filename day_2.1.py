# ANAGRAM Check

while True:

    x = input("Enter string 1 : ")
    y = input("Enter string 2 : ")

    if sorted(x.lower()) == sorted(y.lower()) :
        print("Same Strings")
    else:
        print("Different Strings")


    break

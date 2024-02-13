while True:
    x = float(input("Enter Number : "))

    if x == 0:
        print("Number is 0")
    elif x % 2 != 0:
        print("It's an Odd Number")
    elif x % 2 == 0:
        print("It's an Even Number")
    else:
        print("It's a negative Number")

    another_input = input("Do you want to enter another number : ").lower()

    if another_input != "yes":
        break


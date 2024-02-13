# ODD/EVEN Number Identifying 
while True:
    
    x = float(input("Enter Number : "))
    
    if x ==0:
        print("Number is 0")
    elif x%2 != 0:
        print("Its a Odd Number")
    elif x%2==0:
        print("Its a Even Number")
    else:
        print("Its a negative Number")

    another_input = input("another number (yes/no) : ").lower()

    if another_input != "yes":
        break


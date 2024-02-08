# SIMPLE CALCUALTOR 

def add(a , b):
    return(a + b)

def sub( a, b):
    return(a - b)


def mul(a, b):
    return(a * b)

def div(a, b):
    if b != 0:
        return(a / b)
    else:
        return("Cannot divide by 0")


# Get user input for the numbers
num1 = float(input("Enter your first Number : "))
num2 = float(input("Enter your second Number : "))
operation = input("(+, -, *, /)")

# Perform the calcuations 
if operation == "+":
    result = add(num1 , num2)
elif operation == "-":
    result = sub(num1 , num2)
elif operation == "*":
    result = mul(num1 , num2)
elif operation == '/':
    result = div(num1, num2)
else:
    print("Not valid Calculation")
    
print(result)

# Ask if users wants to one more calculations 
another_calcuation = input("One More Calculation (Yes/No) : ").lower()
if another_calcuation != "yes":
    print("thank you")

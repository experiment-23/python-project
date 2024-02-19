# FizzBuzz: Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".



while True:
    print("Hi")

    for i in range(1,101,1):
        if i % 3 == 0 and i % 5 ==0:
                print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)



    else: 
        print("Thank you")
        break

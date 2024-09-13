'''Calculator for math operation '''

print("Hallo, Here is the calculator")
print("Please choose one of the following operations:")
print("Add(A), Subtract(S), Multiply(M), Divide(D)")
operation: str = input()

if operation == "A":
    print("You have chosen Add")
    print("Please enter two numbers to add!")
    number1 = int(input())
    number2 = int(input())
    print(number1 + number2)

elif operation == "S":
    print("You have chosen subtract")
    print("please enter tow numbers to subtract")
    number1 = int(input())
    number2 = int(input())
    print(number1 - number2)
elif operation == "M":
    print("You have chosen multiply")
    print("please enter tow numbers to multiply")
    number1 = input()
    number2 = input()
    print(int(number1) * int(number2))
elif operation == "D":
    print("you have chosen divide  ")
    print("please enter tow numbers to divide:")
    number1 = int(input())
    number2 = int(input())
    print(number1 / number2)
else:
    print("Your input was incorrect. Please restart the program!")

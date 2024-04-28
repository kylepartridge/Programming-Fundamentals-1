# Name: Kyle Partridge
# Date: 01/19/2024
# Lab 2: Calculator

first = float(input("Enter first operand: ")) # User enters operands
second = float(input("Enter second operand: "))
print("")
print("Calculator Menu\n---------------")   # Display the menu options
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
print("Which operation do you want to perform?", end = " ")
option = int(input())   # User picks an operation

# If a user enters 1, 2, 3 or 4, execute the nested if statements. If user does not enter 1, 2, 3 or 4, print an error statement
if option == 1 or option == 2 or option == 3 or option == 4:
    if option == 1:
        answer = first + second
        print(f"The result of the operation is {answer}. Goodbye!")
    if option == 2:
        answer = first - second
        print(f"The result of the operation is {answer}. Goodbye!")
    if option == 3:
        answer = first * second
        print(f"The result of the operation is {answer}. Goodbye!")
    if option == 4:
        answer = first / second
        print(f"The result of the operation is {answer}. Goodbye!")
else:
    print("Error: Invalid selection! Terminating program.")

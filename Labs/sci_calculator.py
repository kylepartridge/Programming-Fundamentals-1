# Import math module
import math
# Define function to print the menu
def menu() :
    print('Calculator Menu\n---------------')
    print('0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n'
          '4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average')
# Define starting values for result, sum of results and count
current_result = 0.0
results_added = 0
count = 0
print(f"Current Result: {current_result}\n")
menu()
print()
# Enter menu selection
selection = int(input('Enter Menu Selection: '))

# Execute inputted operation using if statements. Increase the count.
# Add the result to the sum of results
# For each selection, if RESULT is inputted as operand. Call the current result.
while True:
    # Exit program
    if selection == 0:
        print('Thanks for using this calculator. Goodbye!')
        break
    # Addition
    elif selection == 1:
        first_operand = input('Enter first operand: ')
        second_operand = input('Enter second operand: ')
        if first_operand == 'RESULT' and second_operand == 'RESULT':
            first_operand = current_result
            second_operand = current_result
        elif first_operand == 'RESULT':
            first_operand = current_result
            second_operand = float(second_operand)
        elif second_operand == 'RESULT':
            first_operand = float(first_operand)
            second_operand = current_result
        else:
            first_operand = float(first_operand)
            second_operand = float(second_operand)
        print()
        current_result = first_operand + second_operand
        results_added += current_result
        count += 1
        print(f"Current Result: {current_result}")
        print()
        menu()
    # Subtraction
    elif selection == 2:
        first_operand = input('Enter first operand: ')
        second_operand = input('Enter second operand: ')
        if first_operand == 'RESULT' and second_operand == 'RESULT':
            first_operand = current_result
            second_operand = current_result
        elif first_operand == 'RESULT':
            first_operand = current_result
            second_operand = float(second_operand)
        elif second_operand == 'RESULT':
            first_operand = float(first_operand)
            second_operand = current_result
        else:
            first_operand = float(first_operand)
            second_operand = float(second_operand)
        print()
        current_result = first_operand - second_operand
        results_added += current_result
        count += 1
        print(f"Current Result: {current_result}")
        print()
        menu()
    # Multiplication
    elif selection == 3:
        first_operand = input('Enter first operand: ')
        second_operand = input('Enter second operand: ')
        if first_operand == 'RESULT' and second_operand == 'RESULT':
            first_operand = current_result
            second_operand = current_result
        elif first_operand == 'RESULT':
            first_operand = current_result
            second_operand = float(second_operand)
        elif second_operand == 'RESULT':
            first_operand = float(first_operand)
            second_operand = current_result
        else:
            first_operand = float(first_operand)
            second_operand = float(second_operand)
        print()
        current_result = first_operand * second_operand
        results_added += current_result
        count += 1
        print(f"Current Result: {current_result}")
        print()
        menu()
    # Division
    elif selection == 4:
        first_operand = input('Enter first operand: ')
        second_operand = input('Enter second operand: ')
        if first_operand == 'RESULT' and second_operand == 'RESULT':
            first_operand = current_result
            second_operand = current_result
        elif first_operand == 'RESULT':
            first_operand = current_result
            second_operand = float(second_operand)
        elif second_operand == 'RESULT':
            first_operand = float(first_operand)
            second_operand = current_result
        else:
            first_operand = float(first_operand)
            second_operand = float(second_operand)
        print()
        current_result = first_operand / second_operand
        results_added += current_result
        count += 1
        print(f"Current Result: {current_result}")
        print()
        menu()
    # Exponentiation
    elif selection == 5:
        first_operand = input('Enter first operand: ')
        second_operand = input('Enter second operand: ')
        if first_operand == 'RESULT' and second_operand == 'RESULT':
            first_operand = current_result
            second_operand = current_result
        elif first_operand == 'RESULT':
            first_operand = current_result
            second_operand = float(second_operand)
        elif second_operand == 'RESULT':
            first_operand = float(first_operand)
            second_operand = current_result
        else:
            first_operand = float(first_operand)
            second_operand = float(second_operand)
        print()
        current_result = math.pow(first_operand, second_operand)
        results_added += current_result
        count += 1
        print(f"Current Result: {current_result}")
        print()
        menu()
    # Logarithm
    elif selection == 6:
        first_operand = input('Enter first operand: ')
        second_operand = input('Enter second operand: ')
        if first_operand == 'RESULT' and second_operand == 'RESULT':
            first_operand = current_result
            second_operand = current_result
        elif first_operand == 'RESULT':
            first_operand = current_result
            second_operand = float(second_operand)
        elif second_operand == 'RESULT':
            first_operand = float(first_operand)
            second_operand = current_result
        else:
            first_operand = float(first_operand)
            second_operand = float(second_operand)
        print()
        current_result = math.log(second_operand, (first_operand))
        results_added += current_result
        count += 1
        print(f"Current Result: {current_result}")
        print()
        menu()
    # Compute average unless there are no calculations to average
    elif selection == 7:
        if count == 0:
            print('Error: No calculations yet to average!\n')
        else:
            print(f"Sum of calculations: {results_added}")
            print(f"Number of calculations: {count}")
            #average = results_added/count
            print(f"Average of calculations: {results_added/count:.2f}")
            print()
    # Error message for invalid inputs
    else:
        print('Error: Invalid selection!')
        print()
    # Ask for the next menu selection
    selection = int(input('Enter Menu Selection: '))




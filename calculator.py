"""
Author: Usman Farooq
"""

"""
Defined the functions below, and added the equations
"""

def add(x, y): 
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y): 
    if y == 0:
        return "Error: Division by zero"
    return x / y

def display_result(operation, result):
    print(f"\n{operation} Result: {result}")



def calculator():
    print("\n-------------------------")
    print("    Welcome to CoolCalc!")
    print("-------------------------")
    

    while True:
        print("\nAvailable Operations:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (x)")
        print("4. Divide (/)")
        print("5. Exit")

    # Calculator options given above

        try:
            choice = int(input("\nChoose an operation (1/2/3/4/5): "))
            
            if choice == 5:
                print("\nThanks for using CoolCalc! Goodbye!")
                break
            
            a = float(input("\nEnter the first number: "))
            b = float(input("Enter the second number: "))
            
            if choice == 1:
                result = add(a, b)
                display_result("Sum", result)
            elif choice == 2:
                result = subtract(a, b)
                display_result("Difference", result)
            elif choice == 3:
                result = multiply(a, b)
                display_result("Product", result)
            elif choice == 4:
                result = divide(a, b)
                display_result("Quotient", result)
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("\nError: Invalid input. Please enter numeric values.")

if __name__ == "__main__": # Added main guard
    calculator()
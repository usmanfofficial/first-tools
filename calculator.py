"""
Author: Usman Farooq
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
        
        try:
            choice = int(input("\nChoose an operation (1/2/3/4/5): "))
            
            if choice == 5:
                print("\nThanks for using CoolCalc! Goodbye!")
                break
            
            a = float(input("\nEnter the first number: "))
            b = float(input("Enter the second number: "))
            
           
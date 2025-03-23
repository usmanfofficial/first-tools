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

def main(): # defined main
    print("Simple Calculator")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        print(f"Sum: {add(a, b)}")
        print(f"Difference: {subtract(a, b)}")
        print(f"Product: {multiply(a, b)}")
        print(f"Quotient: {divide(a, b)}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

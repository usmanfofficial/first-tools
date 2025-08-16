def add(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        print(add(float(sys.argv[1]), float(sys.argv[2])))
    else:
        print("Usage: python calculator.py 2 3")

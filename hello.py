def greet(name):
    """
        Gretting user with personalised message
    """
    return f"Hello, {name}! Welcome to my first GitHub repo."

def main():
    user = input("Enter your name: ")
    print(greet(user))

if __name__ == "__main__":
    main()

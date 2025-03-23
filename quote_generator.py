import random  

quotes = [
    "Believe you can and you're halfway there.",  # Quote by Theodore Roosevelt
    "The only way to do great work is to love what you do.",  # Quote by Steve Jobs
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",  # Quote by Winston Churchill
    "Do what you can, with what you have, where you are.",  # Quote by Theodore Roosevelt
    "It does not matter how slowly you go as long as you do not stop.",  # Quote by Confucius
    "Hardships often prepare ordinary people for an extraordinary destiny.",  # Quote by C.S. Lewis
    "Dream big and dare to fail.",  # Quote by Norman Vaughan
    "Opportunities don't happen, you create them."  # Quote by Chris Grosser
]

def get_quote():
    # Use random.choice() to pick a random quote from the quotes list
    return random.choice(quotes)

def main():
    # Print a random quote when the script is run directly
    print(get_quote())

    # Asking the user if they want another quote
    while True:
        user_input = input("Would you like another quote? (yes/no): ").strip().lower()
        if user_input == 'yes':
            print(get_quote())
        elif user_input == 'no':
            print("Thank you for using the quote generator. Have a great day!")
            break  # Break the loop to end the program
        else:
            # If the user input is invalid, ask again
            print("Please enter 'yes' or 'no'.")

# Main execution block
if __name__ == "__main__":
    main()
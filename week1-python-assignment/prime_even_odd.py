def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_prime(number):
    if number <= 1:
        return False

    limit = int(number ** 0.5) + 1
    for i in range(2, limit):
        if number % i == 0:
            return False 
            
    return True  

def main():
    print("=== Even/Odd & Prime Number Checker ===")
    
    while True:
        user_input = input("\nEnter an integer to check (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
            
        try:
            number = int(user_input)

            if is_even(number):
                parity = "Even"
            else:
                parity = "Odd"

            if is_prime(number):
                primality = "a Prime number"
            else:
                primality = "NOT a Prime number"

            print(f"Result: {number} is an {parity} number and is {primality}.")
            
        except ValueError:
            print("Error: Please enter a valid integer (whole number).")

if __name__ == "__main__":
    main()
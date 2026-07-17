import math

def calculate_circle_area(radius):
    if radius < 0:
        return "Error: Radius cannot be negative."
    area = math.pi * (radius ** 2)
    return area

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def calculate_factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

def count_vowels_consonants(text):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count

def generate_fibonacci(terms):
    if terms <= 0:
        return []
    elif terms == 1:
        return [0]

    series = [0, 1]

    for _ in range(2, terms):
        next_term = series[-1] + series[-2]
        series.append(next_term)
        
    return series

def main():
    while True:
        print("\n=== Practice Questions Suite ===")
        print("1. Calculate Area of Circle")
        print("2. Check Even or Odd")
        print("3. Calculate Factorial (using Recursion)")
        print("4. Count Vowels and Consonants")
        print("5. Generate Fibonacci Series")
        print("6. Exit")
        
        choice = input("Choose a program to test (1-6): ").strip()
        
        if choice == '1':
            try:
                r = float(input("Enter radius: "))
                area = calculate_circle_area(r)
                if isinstance(area, str): 
                    print(area)
                else:
                    print(f"Area of circle: {area:.4f}")
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '2':
            try:
                num = int(input("Enter an integer: "))
                result = check_even_odd(num)
                print(f"The number {num} is {result}.")
            except ValueError:
                print("Error: Please enter a valid integer.")
                
        elif choice == '3':
            try:
                num = int(input("Enter a positive integer: "))
                result = calculate_factorial(num)
                print(f"Factorial of {num} is: {result}")
            except ValueError:
                print("Error: Please enter a valid integer.")
                
        elif choice == '4':
            text = input("Enter any text sentence: ")
            v, c = count_vowels_consonants(text)
            print(f"Vowels: {v}, Consonants: {c}")
            
        elif choice == '5':
            try:
                terms = int(input("Enter the number of terms: "))
                series = generate_fibonacci(terms)
                print(f"Fibonacci series: {series}")
            except ValueError:
                print("Error: Please enter a valid integer.")
                
        elif choice == '6':
            print("Exiting practice suite. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please choose from 1 to 6.")

if __name__ == "__main__":
    main()
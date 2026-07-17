def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        print("\n=== Temperature Converter ===")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                result = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {result:.2f}°F")
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                result = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {result:.2f}°C")
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '3':
            print("Thank you for using the Temperature Converter. Goodbye!")
            break 
            
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
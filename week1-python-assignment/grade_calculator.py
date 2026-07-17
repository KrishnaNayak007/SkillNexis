def determine_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def main():
    print("=== Student Grade Calculator ===")
    
    while True:
        try:
            num_subjects = int(input("Enter the total number of subjects: "))
            if num_subjects > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    marks = []
    
    for i in range(1, num_subjects + 1):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Error: Marks must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid number.")

    total_marks = sum(marks)
    max_possible_marks = num_subjects * 100
    percentage = (total_marks / max_possible_marks) * 100
    average = total_marks / num_subjects
    
    grade = determine_grade(percentage)
    
    print("\n--- Summary of Results ---")
    print(f"Total Marks: {total_marks:.2f} / {max_possible_marks:.2f}")
    print(f"Average Marks: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Final Grade: {grade}")
    print("--------------------------")

if __name__ == "__main__":
    main()
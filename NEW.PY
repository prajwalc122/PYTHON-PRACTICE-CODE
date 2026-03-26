def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

marks = int(input("Enter your marks: "))
grade = calculate_grade(marks)
print("Your Grade:", grade)
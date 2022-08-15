
grade_input = float(input())

def grade_calculation():
    if grade_input < 3:
        return "Fail"
    elif grade_input >= 3 and grade_input < 3.50:
        return "Poor"
    elif grade_input >= 3.5 and grade_input < 4.50:
        return "Good"
    elif grade_input >= 4.50 and grade_input < 5.50:
        return "Very Good"
    elif grade_input >= 5.50:
        return "Excellent"

print(grade_calculation())

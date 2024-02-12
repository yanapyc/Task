def average_grade(student_grades):
    return sum(student_grades.values()) / len(student_grades)

def highest_grade(student_grades):
    return [name for name, grade in student_grades.items() if grade > 90]

def lowest_grade(student_grades):
    return [name for name, grade in student_grades.items() if grade < 90]

def grade_distribution(student_grades):
    failing_grades = [name for name, grade in student_grades.items() if grade < 75]
    passing_grades = [name for name, grade in student_grades.items() if grade >= 75]
    return passing_grades,failing_grades

def improvement_suggestions(student_grades):
    for name,grade in student_grades.items():
        if grade < 85:
            print(f"{name} encouraged to attend additional tutoring sessions!")

def bar_chart(student_grades):
    for name,grade in student_grades.items():
        print(f"{name}: {'=' * (grade // 10)}")   


# Grade Summary
def print_grade_summary(student_grades):
    print("Grade Summary:")
    average = average_grade(student_grades)
    print(f"Average grade: {average:.2f}")

    highest = highest_grade(student_grades)
    highest_students_name = []
    for name in highest:
        highest_students_name.append(name)
    print("Highest grade:", highest_students_name)

    lowest = lowest_grade(student_grades)
    lowest_students_name = []
    for name in lowest:
        lowest_students_name.append(name)
    print("Lowest grade:",lowest_students_name)
    print()

# Grade Distribution
def print_grade_distribution(student_grades):
    passing_students, failing_students = grade_distribution(student_grades)
    print("Grade Distribution:")
    print("Passing students:", passing_students)
    print("Failing students:", failing_students)
    print()

# Improvement Suggestions
def print_improvement_suggestions(student_grades):
    print("Improvement Suggestions:")
    improvement_suggestions(student_grades)
    print()

# Visual Representation
def print_visual_representation(student_grades):
    print("Visual Representation:")
    bar_chart(student_grades)

student_grades = {
    "Alice": 88,
    "Bob": 76,
    "Charlie": 90,
    "Diana": 85,
    "Evan": 92, 
    "Fiona": 79,
    "George": 95
}

print_grade_summary(student_grades)
print_grade_distribution(student_grades)
print_improvement_suggestions(student_grades)
print_visual_representation(student_grades)
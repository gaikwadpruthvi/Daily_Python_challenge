## Student Gradebook
student_grades = {}
print("Student Gradebook")

while True:
    print("\nOptions:")
    print("1. Add ")
    print("2. Search")
    print("3. Display")
    print("4. Exit")
    choice = input("Enter your choice:\n")
    
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        student_grades[name] = grade
    elif choice == "2":
        name = input("Enter student name to search: ")
        print(student_grades.get(name, "Student not found"))
    elif choice == "3":
        print(student_grades)
    elif choice == "4":
        break
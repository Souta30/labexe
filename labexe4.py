# Initialize empty lists and dictionary
students_list = []
students_dict = {}

def add_student():
    # Prompt user for student information
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")

    # Add student information to lists and dictionary
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    print("Student information added successfully.")

def search_student():
    # Prompt user to enter student's name for search
    name = input("Enter student's name to search or simply press Enter to skip: ")

    # Search for student in dictionary
    if name in students_dict:
        print("Name:", name)
        print("Age:", students_dict[name]['age'])
        print("Grade:", students_dict[name]['grade'])
    else:
        print("Student not found!")

def remove_student():
    # Prompt user to enter student's name for removal
    name = input("Enter student's name to remove or simply press Enter to skip: ")

    # Remove student from lists and dictionary if found
    if name in students_list:
        students_list.remove(name)
        del students_dict[name]
        print("Student removed successfully.")
    else:
        print("Student not found!")

# Main program loop
while True:
    print("\n1. Add student\n2. Search student\n3. Remove student\n4. View all students\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        print("Student details:")
        for name, info in students_dict.items():
            print("Name:", name)
            print("Age:", info['age'])
            print("Grade:", info['grade'])
            print()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

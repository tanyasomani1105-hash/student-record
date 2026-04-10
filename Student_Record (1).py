students = [
    {"id": i, "name": f"Student{i}", "age": 18 + (i % 5), "course": "CSE", "grade": chr(65 + (i % 5))}
    for i in range(1, 51)
]

def display_students():
    print("\n--- Student Records ---")
    for student in students:
        print(student)

def add_student():
    print("\nEnter new student details:")
    sid = int(input("ID: "))
    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")
    grade = input("Grade: ")

    students.append({
        "id": sid,
        "name": name,
        "age": age,
        "course": course,
        "grade": grade
    })
    print("Student added successfully!")

def search_student():
    print("\nSearch By:")
    print("1. ID")
    print("2. Name")
    print("3. Age")
    print("4. Course")
    print("5. Grade")

    choice = input("Enter choice: ")
    found = False

    if choice == '1':
        value = int(input("Enter ID: "))
        for s in students:
            if s["id"] == value:
                print(s)
                found = True

    elif choice == '2':
        value = input("Enter Name: ")
        for s in students:
            if s["name"].lower() == value.lower():
                print(s)
                found = True

    elif choice == '3':
        value = int(input("Enter Age: "))
        for s in students:
            if s["age"] == value:
                print(s)
                found = True

    elif choice == '4':
        value = input("Enter Course: ")
        for s in students:
            if s["course"].lower() == value.lower():
                print(s)
                found = True

    elif choice == '5':
        value = input("Enter Grade: ")
        for s in students:
            if s["grade"].upper() == value.upper():
                print(s)
                found = True

    else:
        print("Invalid choice")
        return

    if not found:
        print("No matching student found.")

def update_student():
    sid = int(input("\nEnter Student ID to update: "))
    
    for s in students:
        if s["id"] == sid:
            print("Current Details:", s)

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Course")
            print("4. Grade")

            choice = input("Enter choice: ")

            if choice == '1':
                s["name"] = input("Enter new name: ")
            elif choice == '2':
                s["age"] = int(input("Enter new age: "))
            elif choice == '3':
                s["course"] = input("Enter new course: ")
            elif choice == '4':
                s["grade"] = input("Enter new grade: ")
            else:
                print("Invalid choice")
                return

            print("Student updated successfully!")
            return

    print("Student not found.")

def menu():
    while True:
        print("\n===== Student Record System =====")
        print("1. Display All Students")
        print("2. Add Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")

menu()
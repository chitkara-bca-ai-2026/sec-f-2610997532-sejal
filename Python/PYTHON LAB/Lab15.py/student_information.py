students = {
    101: {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [85, 90, 73]
    },
    102: {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [92, 88, 95]
    },
    103: {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [92, 88, 95]
    }
}


def view_students():
    print("\n========== ENROLLED STUDENTS ==========")

    if not students:
        print("No student records found.")
        return

    for roll, student in students.items():
        print(f"\nRoll No: {roll}")
        print(f"Name: {student['Name']}")
        print(f"Branch: {student['Branch']}")
        print(f"Semester: {student['Semester']}")
        print(f"Marks: {student['Marks']}")

    print(f"\nTotal Enrolled Students: {len(students)}")


def search_student():
    roll = int(input("Enter Roll Number to search: "))

    student = students.get(roll)

    if student:
        print("\n[FOUND] Student Record")
        print("Roll No:", roll)
        print("Name:", student["Name"])
        print("Branch:", student["Branch"])
        print("Semester:", student["Semester"])
        print("Marks:", student["Marks"])
    else:
        print("[ERROR] Student not found!")


def register_student():
    print("\n========== REGISTER NEW STUDENT ==========")

    roll = int(input("Enter Roll Number: "))

    if roll in students:
        print("[ERROR] Roll Number already exists!")
        return

    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    semester = int(input("Enter Semester: "))

    marks = []

    print("Enter marks obtained in 3 subjects:")

    for i in range(3):
        mark = int(input(f"Subject {i+1}: "))
        marks.append(mark)

    students[roll] = {
        "Name": name,
        "Branch": branch,
        "Semester": semester,
        "Marks": marks
    }

    print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")


def update_student():
    roll = int(input("Enter Roll Number to update: "))

    if roll not in students:
        print("[ERROR] Student not found!")
        return

    print("\nCurrent Student Details:")
    print("1. Branch:", students[roll]["Branch"])
    print("2. Semester:", students[roll]["Semester"])

    choice = int(input("Choose field to update (1 for Branch, 2 for Semester): "))

    if choice == 1:
        new_branch = input("Enter new Branch: ")
        students[roll]["Branch"] = new_branch
        print("[SUCCESS] Branch updated successfully.")

    elif choice == 2:
        new_semester = int(input("Enter new Semester: "))
        students[roll]["Semester"] = new_semester
        print(f"[SUCCESS] Semester updated to '{new_semester}'.")

    else:
        print("[ERROR] Invalid choice!")


def academic_performance():
    roll = int(input("Enter Roll Number for Academic Performance: "))

    if roll not in students:
        print("[ERROR] Student not found!")
        return

    student = students[roll]

    total = sum(student["Marks"])
    average = total / len(student["Marks"])

    print("\n" + "=" * 15 + " ACADEMIC REPORT " + "=" * 15)
    print("Student Name :", student["Name"])
    print("Subject Marks:", student["Marks"])
    print("Total Marks  :", total, "/ 300")
    print("Average Marks:", round(average, 2), "%")

    if average >= 40:
        print("Final Result : PASS")
    else:
        print("Final Result : FAIL")

    print("=========================================================")


def delete_student():
    roll = int(input("Enter Roll Number to delete: "))

    if roll in students:
        name = students[roll]["Name"]

        students.pop(roll, None)

        print(f"\n[SUCCESS] Record for '{name}' (Roll No: {roll}) deleted successfully.")

    else:
        print("[ERROR] Student not found!")


while True:

    print("\n=============================================")
    print("STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("===============================================")

    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = int(input("\nEnter your choice (1-7): "))

    if choice == 1:
        view_students()

    elif choice == 2:
        search_student()

    elif choice == 3:
        register_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        academic_performance()

    elif choice == 6:
        delete_student()

    elif choice == 7:
        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please select between 1 and 7.")
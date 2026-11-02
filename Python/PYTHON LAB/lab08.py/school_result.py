print("=========================================")
print("       SCHOOL RESULT PROCESSING")
print("==========================================")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

marks = []

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

for i in range(1, 6):
    m = float(input("Enter marks for Subject " + str(i) + ": "))

    if m < 0 or m > 100:
        print("Invalid marks")
        exit()

    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100

if any(m < 40 for m in marks):
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:
    result = "PASS"

    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remarks = "Pass"
    else:
        grade = "F"
        remarks = "Fail"

print("\n==========================================")
print("          STUDENT REPORT CARD")
print("==========================================")
print("Student Name :", name)
print("Roll Number  :", roll)
print("==========================================")
print("Total Marks  :", total, "/ 500")
print("Percentage   : {:.2f}%".format(percentage))
print("Result       :", result)
print("Grade        :", grade)
print("Remarks      :", remarks)
print("==========================================")
name = input("Enter student name: ")
num_subjects = int(input("Enter number of subjects: "))
total_marks = 0

for i in range(1, num_subjects + 1):
    marks = float(input("Enter marks for subject " + str(i) + ": "))
    total_marks += marks

average = total_marks / num_subjects
percentage = (total_marks / (num_subjects * 100)) * 100

if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B+'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
elif percentage >= 34:
    grade = 'D'
else:
    grade = 'F'

if percentage >= 34:
    status = 'Pass'
else:
    status = 'Fail'

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total_marks)
print("Average:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Status:", status)

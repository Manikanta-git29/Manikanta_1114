import csv


students = [
    [101, "Manikanta", 85, 78, 90, 88],
    [102, "shreya", 92, 89, 95, 91],
    [103, "Rohan", 76, 80, 72, 79],
    [104, "Nani", 88, 84, 86, 90],
    [105, "visva", 70, 75, 68, 72],
    [106, "justin", 95, 96, 94, 98],
    [107, "virat", 82, 79, 85, 81],
    [108, "karan", 90, 88, 87, 92],
    [109, "Arjun", 78, 74, 80, 76],
    [110, "Priya", 86, 89, 84, 88]
]

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Subject1", "Subject2", "Subject3", "Subject4"])
    writer.writerows(students)

print("student.csv file created successfully.\n")


print("Student Records:")
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


highest_student = None
highest_total = 0

with open("student.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    total_marks_all = 0
    student_count = 0

    for row in reader:
        marks = list(map(int, row[2:]))
        total = sum(marks)

        total_marks_all += total
        student_count += 1

        if total > highest_total:
            highest_total = total
            highest_student = row

average_marks = total_marks_all / student_count

print("\nHighest Scorer:")
print("Roll No:", highest_student[0])
print("Name:", highest_student[1])
print("Total Marks:", highest_total)

print("\nAverage Marks of All Students:", round(average_marks, 2))
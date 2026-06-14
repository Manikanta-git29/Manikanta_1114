# FILE HANDLING PROGRAMS IN ONE FILE

# 1. Create student.txt and store 5 student names

file = open("student.txt", "w")

for i in range(5):
    name = input(f"Enter student name {i+1}: ")
    file.write(name + "\n")

file.close()
print("File created successfully!")

print("="*50)


# 2. Read and display entire file

file = open("student.txt", "r")
data = file.read()
print("File Contents:")
print(data)
file.close()

print("="*50)


# 3. Count total characters

file = open("student.txt", "r")
data = file.read()
print("Total Characters:", len(data))
file.close()

print("="*50)


# 4. Count total lines

file = open("student.txt", "r")
lines = file.readlines()
print("Total Lines:", len(lines))
file.close()

print("="*50)


# 5. Count total words

file = open("student.txt", "r")
data = file.read()
words = data.split()
print("Total Words:", len(words))
file.close()

print("\n" + "="*40)

print("="*50)


# 6. Count frequency of each character

file = open("student.txt", "r")
data = file.read()

freq = {}

for ch in data:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequencies:")
for key, value in freq.items():
    print(key, ":", value)

file.close()

print("="*50)


# 7. Append Data

file = open("student.txt", "a")
for i in range(3):
    data = input("Enter new record: ")
    file.write(data + "\n")
file.close()

print("="*50)


# 8. Search a Word

file = open("student.txt", "r")
data = file.read()
word = input("Enter word to search: ")

if word in data:
    print("Word Found")
else:
    print("Word Not Found")

file.close()


print("="*50)


# 9. Count Vowels

file = open("student.txt", "r")
data = file.read()

count = 0
for ch in data:
    if ch in "aeiouAEIOU":
        count += 1

print("Total Vowels:", count)
file.close()


print("="*50)

# 10. Count Uppercase and Lowercase Letters

file = open("student.txt", "r")
data = file.read()

upper = 0
lower = 0

for ch in data:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)

file.close()


print("="*50)


# 11. Display Longest Line

file = open("student.txt", "r")
lines = file.readlines()

longest = ""

for line in lines:
    if len(line) > len(longest):
        longest = line

print("Longest Line:")
print(longest)

file.close()

print("="*50)


# 12. Copy File Content

source = open("student.txt", "r")
data = source.read()
source.close()

destination = open("copy.txt", "w")
destination.write(data)
destination.close()

print("File copied successfully")

# 13. Replace a Word
file = open("student.txt", "r")
data = file.read()
file.close()

data = data.replace("Python", "Programming")

file = open("student.txt", "w")
file.write(data)
file.close()

print("Word replaced successfully")


print("="*50)


# 14. Store and Read Marks

file = open("marks.txt", "w")

for i in range(10):
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    file.write(name + "," + str(marks) + "\n")

file.close()

print("Students scoring above 75:")

file = open("marks.txt", "r")

for line in file:
    name, marks = line.strip().split(",")
    if int(marks) > 75:
        print(name, marks)

file.close()


print("="*50)


# 15. Binary File (Employee Records)

import pickle

emp = []
n = int(input("Enter number of employees: "))

for i in range(n):
    empid = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    emp.append([empid, name])

file = open("employee.dat", "wb")
pickle.dump(emp, file)
file.close()

search_id = int(input("Enter Employee ID to search: "))

file = open("employee.dat", "rb")
data = pickle.load(file)

found = False

for record in data:
    if record[0] == search_id:
        print("Record Found:", record)
        found = True

if not found:
    print("Record Not Found")

file.close()

print("="*50)

# 16. Count Blank Lines

file = open("student.txt", "r")

blank = 0

for line in file:
    if line.strip() == "":
        blank += 1

print("Blank Lines:", blank)

file.close()


print("="*50)


# 17. Count Digits, Alphabets and Special Characters

file = open("student.txt", "r")
data = file.read()

digits = 0
alphabets = 0
special = 0

for ch in data:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets += 1
    else:
        special += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special Characters:", special)

file.close()

print("="*50)


# 18. Display Lines Starting with a Vowel

file = open("student.txt", "r")

for line in file:
    stripped = line.strip()
    if stripped and stripped[0] in "aeiouAEIOU":
        print(stripped)

file.close()

print("="*50)


# 19. Count Frequency of a Given Word

file = open("student.txt", "r")
data = file.read()
file.close()

word = input("Enter word to count: ")
count = data.lower().split().count(word.lower())
print("Frequency of", word, ":", count)

print("="*50)


# 20. Create Student Result File

file = open("results.txt", "w")

max_total = 0
topper = ""

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter Name: ")
    physics = int(input("Enter Physics Marks: "))
    chemistry = int(input("Enter Chemistry Marks: "))
    maths = int(input("Enter Maths Marks: "))
    total = physics + chemistry + maths
    file.write(name + "," + str(physics) + "," + str(chemistry) + "," + str(maths) + "," + str(total) + "\n")
    if total > max_total:
        max_total = total
        topper = name

file.close()

print("Topper:", topper, "with total marks:", max_total)

print("="*50)


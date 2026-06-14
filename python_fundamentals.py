# 26. Reverse a Number

num = int(input("Enter a number: "))
rev = int(str(num)[::-1])
print("Reversed Number =", rev)

print("="*50)


# 27. Check Palindrome Number

num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print("="*50)


# 28. Count Digits in a Number

num = input("Enter a number: ")
print("Number of digits =", len(num))

print("="*50)

# 29. Sum of Digits
num = input("Enter a number: ")
total = 0
for i in num:
    total += int(i)
print("Sum of digits =", total)

print("="*50)


# 30. Fibonacci Series

n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

print("="*50)


# 31. Check Prime Number

num = int(input("Enter a number: "))
prime = True

if num <= 1:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")

print("="*50)


# 32. Prime Numbers Between 1 and 100

print("Prime Numbers from 1 to 100:")
for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
print()

print("="*50)


# 33. Count Vowels in a String

text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels =", count)

print("="*50)


# 34. Reverse a String

text = input("Enter a string: ")
print("Reversed String =", text[::-1])

print("="*50)


# 35. Count Frequency of Each Character

text = input("Enter a string: ")

for ch in set(text):
    print(ch, "=", text.count(ch))
# DAY 3 - LOOPS

# 11. Print Numbers from 1 to 100
print("\nNumbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")

print("="*50)

# 12. Print Even Numbers Between 1 and 100

print("\n\nEven Numbers from 1 to 100:")
for i in range(2, 101, 2):
    print(i, end=" ")

print("="*50)

# 13. Sum of First N Natural Numbers

n = int(input("\n\nEnter N: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print("Sum =", sum_n)

print("="*50)

# 14. Multiplication Table

num = int(input("\nEnter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("="*50)

# 15. Factorial of a Number

num = int(input("\nEnter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)
# DAY 2 - CONDITIONS


# 6. Check Positive, Negative, or Zero

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("="*50)

# 7. Largest Among Two Numbers

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)

print("="*50)

# 8. Largest Among Three Numbers

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

print("="*50)

# 9. Check Even or Odd

num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("="*50)

# 10. Check Leap Year

year = int(input("\nEnter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
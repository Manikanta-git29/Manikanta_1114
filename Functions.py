# DAY 4 - FUNCTIONS

# 16. Function to find square of a number

def square(n):
    return n * n

num = int(input("Enter a number: "))
print("Square =", square(num))

print("="*50)

# 17. Function to find maximum of two numbers

def maximum(a, b):
    return a if a > b else b

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("Maximum =", maximum(a, b))

print("="*50)

# 18. Function to calculate simple interest

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("\nEnter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
print("Simple Interest =", simple_interest(p, r, t))

print("="*50)

# 19. Function to check even or odd

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

num = int(input("\nEnter a number: "))
print(check_even_odd(num))

print("="*50)

# 20. Function to calculate area of a circle

def area_circle(radius):
    return 3.14 * radius * radius

radius = float(input("\nEnter radius: "))
print("Area of Circle =", area_circle(radius))



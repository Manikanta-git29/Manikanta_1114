# DAY 1 - Variables, Data Types, I/O, Operator

# 1. Sum of Two Numbers

print("1. Sum of Two Numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum =", num1 + num2)

print("\n-------------------")



# 2. Area of a Rectangle

print("2. Area of Rectangle")
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area =", area)

print("\n-------------------")


# 3. Simple Interest

print("3. Simple Interest")
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))
si = (p * r * t) / 100
print("Simple Interest =", si)

print("\n-------------------")



# 4. Celsius to Fahrenheit

print("4. Celsius to Fahrenheit")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

print("\n-------------------")



# 5. Employee Salary Calculation

print("5. Employee Salary Calculation")
basic_salary = float(input("Enter Basic Salary: "))

hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100
gross_salary = basic_salary + hra + da

print("HRA =", hra)
print("DA =", da)
print("Gross Salary =", gross_salary)
# DAY 5 - LISTS, TUPLES, DICTIONARY, SET

# 21. Create a list of 10 numbers and print all elements

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nList Elements:")
for num in numbers:
    print(num, end=" ")


# 22. Find largest element in a list

print("\n\nLargest Element =", max(numbers))

print("="*50)

# 23. Calculate sum of all elements in a list

print("Sum of Elements =", sum(numbers))

print("="*50)

# 24. Count even numbers in a list

count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1

print("Count of Even Numbers =", count)

print("="*50)


# 25. Program to remove duplicate elements using sets

numbers = [10, 20, 30, 20, 40, 10, 50, 30]

unique_numbers = list(set(numbers))

print("Original List:", numbers)
print("List after removing duplicates:", unique_numbers)
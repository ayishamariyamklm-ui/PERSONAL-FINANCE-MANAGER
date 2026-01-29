# ============================================
# Mini Practice Tasks
# ============================================

# Task 1: Check even or odd
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Task 2: Sum of numbers in a list
numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total += num

print("Sum:", total)


# Task 3: Find largest number
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)


# Task 4: Count vowels in a string
text = "Python Programming"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowel count:", count)


# Task 5: Simple dictionary usage
student = {"name": "Ayisha", "marks": 85}

if student["marks"] >= 50:
    print("Pass")
else:
    print("Fail")

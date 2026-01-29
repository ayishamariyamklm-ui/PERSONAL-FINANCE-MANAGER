# ============================================
# Python Syntax & Data Structures
# ============================================

print("PYTHON BASICS DEMONSTRATION\n")

# --------------------------------------------
# 1. VARIABLES & DATA TYPES
# --------------------------------------------

# Integer
age = 22
print("Age:", age, "| Type:", type(age))

# Float
height = 5.4
print("Height:", height, "| Type:", type(height))

# String
name = "Ayisha"
print("Name:", name, "| Type:", type(name))

# Boolean
is_student = True
print("Is Student:", is_student, "| Type:", type(is_student))

print("\n--------------------------------------------")

# --------------------------------------------
# 2. LIST
# --------------------------------------------
# Features: Ordered, mutable, allows duplicates

subjects = ["Maths", "Physics", "Computer Science"]
print("Subjects List:", subjects)

# Access element
print("First subject:", subjects[0])

# Add element
subjects.append("Data Science")
print("After adding:", subjects)

print("\n--------------------------------------------")

# --------------------------------------------
# 3. TUPLE
# --------------------------------------------
# Features: Ordered, immutable

coordinates = (10, 20)
print("Coordinates Tuple:", coordinates)
print("X coordinate:", coordinates[0])

print("\n--------------------------------------------")

# --------------------------------------------
# 4. SET
# --------------------------------------------
# Features: Unordered, unique elements

unique_numbers = {1, 2, 3, 3, 4}
print("Unique Numbers Set:", unique_numbers)

# Add element
unique_numbers.add(5)
print("After adding:", unique_numbers)

print("\n--------------------------------------------")

# --------------------------------------------
# 5. DICTIONARY
# --------------------------------------------
# Feature: Key-value pairs

student = {
    "name": "Ayisha",
    "age": 22,
    "course": "Data Science"
}

print("Student Dictionary:", student)
print("Student Name:", student["name"])

print("\n--------------------------------------------")

# --------------------------------------------
# 6. CONDITIONAL STATEMENTS
# --------------------------------------------

marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")

print("\n--------------------------------------------")

# --------------------------------------------
# 7. FOR LOOP
# --------------------------------------------

print("For Loop Example:")
for subject in subjects:
    print(subject)

print("\n--------------------------------------------")

# --------------------------------------------
# 8. WHILE LOOP
# --------------------------------------------

print("While Loop Example:")
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

print("\n--------------------------------------------")

# --------------------------------------------
# 9. USER INPUT METHOD
# --------------------------------------------

name = input("Enter your name: ")
print("Welcome", name)

# --------------------------------------------
# Using string :

age = int(input("Enter age: "))
print(age + 1)

print("\n--------------------------------------------")

# --------------------------------------------
# 10. ARITHMETIC OPERATIONS
# --------------------------------------------

x = 10
y = 3

print(x + y)   # Addition
print(x - y)   # Subtraction
print(x * y)   # Multiplication
print(x / y)   # Division
print(x % y)   # Modulus
print(x ** y)  # Power

print("\n--------------------------------------------")

# --------------------------------------------
# 11. RANGE : NUMBER SEQUENCE
# --------------------------------------------

for i in range(5):
    print(i)

print("\n--------------------------------------------")    

# --------------------------------------------
# 12. BREAK & CONTINUE 
# --------------------------------------------

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\n--------------------------------------------") 

# --------------------------------------------
# 13. IMPORT - USING BILD IN MODULES
# --------------------------------------------

import math

print(math.sqrt(16))

print("\n--------------------------------------------") 

# ============================================
# Class Creation 
# ============================================

class Student:
    """
    This class represents a student.
    """

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display details
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# -------- Main Program --------

# Create object of the class
student1 = Student("Ayisha", 22)

# Call class method
student1.display_details()



print("END OF PYTHON BASICS")

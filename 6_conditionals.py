# Simple if-else
age = int(input("Enter your age: "))
if age >= 30:
    print("Senior")
else:
    print("Junior")

print("\n")

# if-elif-else example
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

print("\n")

# Nested if example
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif num == 0:
    print("Zero")
else:
    print("Negative")
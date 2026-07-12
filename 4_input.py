# Basic string input
name = input("Enter your name: ")
print("Hello,", name)

# Integer input with type casting
num = int(input("Enter a number: "))
print("Square:", num * num)

# Multiple integer inputs
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# Float input
pi = float(input("Enter value of pi: "))
print("Pi =", pi)

# String input example
fav_lang = input("Enter your favorite language: ")
print("You love", fav_lang)

# Input with formatted output
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Mixing predefined and user input
firstNum = 10
secondNum = int(input("Enter another number: "))
print("Sum:", firstNum + secondNum)

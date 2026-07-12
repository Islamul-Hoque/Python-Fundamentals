# For Loop (basic range)
for i in range(5):
    print(i)   # 0 1 2 3 4

print("\n")


# For Loop (custom start and end)
for i in range(1, 6):
    print(i)   # 1 2 3 4 5

print("\n")


# For Loop (odd numbers)
for i in range(1, 6, 2):
    print(i)   # 1 3 5

print("\n")


# For Loop (even numbers)
for i in range(2, 7, 2):
    print(i)   # 2 4 6

print("\n")


# Sum of odd numbers using continue
sum = 0
for i in range(1, 11):
    if i % 2 == 0:
        continue
    else:
        sum += i
print("Odd sum with continue:", sum)


# Alternative odd sum
sum1 = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum1 += i
print("Odd sum alternative:", sum1)

print("\n")


# While Loop (sum of even numbers)
s = 0
i = 2
while i < 101:
    s += i
    i += 2
print("Even sum (while loop):", s)

print("\n")


# Break example
for i in range(1, 10):
    if i == 5:
        print("Breaking at:", i)
        break
    print(i)

print("\n")


# Continue example
for i in range(1, 10):
    if i == 5:
        print("Skipping:", i)
        continue
    print(i)


print("\n")

# Infinite loop example (use with caution)
# Uncomment to test
# while True:
#     print("This will run forever")

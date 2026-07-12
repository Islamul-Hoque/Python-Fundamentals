# Loop through a list

fruits = ["mango", "banana", "jack"]

# Print each fruit using for loop
for fruit in fruits:
    print(fruit)

print("\n")

# Print with index
for i in range(len(fruits)):
    print(f"Index {i} -> {fruits[i]}")

print("\n")

# Using enumerate for cleaner index + value
for idx, fruit in enumerate(fruits):
    print(f"Index {idx} -> {fruit}")

print("\n")

# Check if a fruit exists
search = "banana"
if search in fruits:
    print(search, "is in the list")
else:
    print(search, "not found")

print("\n")

# Add new fruit and loop again
fruits.append("apple")
for fruit in fruits:
    print(fruit)

# Array Program

name = "ARAKAWA"
array = []

# Add each letter
for letter in name:
    array.append(letter)

print("Array:", array)

# Remove each letter until empty
while len(array) > 0:
    array.pop(0)
    print("Array:", array)

print("Array is empty.")
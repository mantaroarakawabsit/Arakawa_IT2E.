# Stack Program

name = "ARAKAWA"
stack = []

# Add each letter
for letter in name:
    stack.append(letter)

print("Stack:", stack)

# Remove each letter until empty
while len(stack) > 0:
    stack.pop()
    print("Stack:", stack)

print("Stack is empty.")
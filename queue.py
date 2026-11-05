# Queue Program

from collections import deque

name = "ARAKAWA"
queue = deque()

# Add each letter
for letter in name:
    queue.append(letter)

print("Queue:", list(queue))

# Remove each letter until empty
while len(queue) > 0:
    queue.popleft()
    print("Queue:", list(queue))

print("Queue is empty.")
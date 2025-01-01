queue = []

n = int(input("Enter the size of the queue: "))
for i in range(n):
    element = input(f"Enter the element {i+1}: ")
    queue.append(element)

print("Initial queue:")
print(queue)

print("\nElements dequeued from queue:")
while queue:
    print(queue.pop(0))

print("\n queue after removing elements:")
print(queue)

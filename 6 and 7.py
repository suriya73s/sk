stack = []

n = int(input("Enter the size: "))
for i in range(n):
    element = input(f"Enter the element {i+1}: ")
    stack.append(element)

print("Initial stack:")
print(stack)

print("\nElements popped from stack:")
while stack:
    print(stack.pop())

print("\nStack after elements are popped:")
print(stack)

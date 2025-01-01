from queue import Queue

q = Queue(maxsize=3)
print(q.qsize())

n = int(input("Enter the number of elements: "))

for i in range(n):
    element = input("Enter the element: ")
    q.put(element)

print("\nFull:", q.full())

print("\nElements dequeued from the queue:")
while not q.empty():
    print(q.get())

print("\nEmpty:", q.empty())
q.put(1)
print("\nFull:", q.full())

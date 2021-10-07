import random

n = int(input("How many darts: "))
inside = 0
for i in range(n):
    x = random.random()
    y = random.random()
    if x * x + y * y < 1:
        inside += 1
result = 4 * inside / n
print(f"Result: {result}")
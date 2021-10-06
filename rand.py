import random

#random.seed(1234)
for i in range(10):
    x = random.randint(1, 6)
    print(x)


colors = ["green", "blue" , "red", "orange", "purple"]
print(random.choice(colors))
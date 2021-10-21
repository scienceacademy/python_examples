f = open("data.txt", "w")
f.write("goodbye")
f.close()

with open("data.txt", "r") as f:
    data = f.read()
print(data)
print("Enter two numbers")
x = int(input("x: "))
y = int(input("y: "))

if x > y:
    print("x is bigger")
elif y > x:
    print("y is bigger")
else:
    print("they're the same")

age = int(input("How old are you? "))
if age > 12 and age < 20:
    print("You're a teenage")
num = 0
while num < 1:
    try:
        num = int(input("Pick a positive number: "))
    except:
        print("That's not an integer.")
print(f"You picked {num}.")
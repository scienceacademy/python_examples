num = 0
while num < 1 or num > 10:
    try:
        num = int(input("Pick an integer from 1 to 10: "))
    except:
        print("That's not an integer.")
print(f"You picked {num}.")
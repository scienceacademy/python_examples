choice = ""
good_choices = ["y", "n", "yes", "no"]
while choice not in good_choices:
    choice = input("Choose yes or no: ").lower()
print("Thanks for answering.")
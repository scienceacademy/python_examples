grades = [95, 94, 60, 83, 50]
names = ["bob", "alice", "eve", "joe", "susan"]

grades = {"alice": 94, "bob": 95, "eve": 60,
"joe": 83, "susan":50}
# look up a grade
name = input("Name: ")
print(grades[name])
# print all grades
for name in grades:
    print(name, grades[name])
# add a new student
name = input("New name: ")
grade = int(input("New grade:"))
grades[name] = grade
print(grades)
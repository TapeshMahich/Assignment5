mark_sheet = {'John' : 98.3,
              'Carol' : 78.4,
              'Tom' : 89.5,
              'Alice':85}

name = input("Enter the student's name: ")
if  name in mark_sheet:
    marks = mark_sheet[name]
    print(f"{name}'s marks:  {marks} ")

else:
    print("Student not found")

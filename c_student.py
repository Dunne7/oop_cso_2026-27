#Exercise B4) Amending nested Data

#List of Student names and their grades
students = [
 {"name": "Evan", "marks": [65, 72, 81]},
 {"name": "Caleb", "marks": [45, 51, 48]},
 {"name": "Angelo", "marks": [82,  77, 91]},
 {"name": "Dorothy", "marks": [55, 63, 59]}
]

def add_mark(student_dict, new_mark):
  add_mark(students[1], 66)
  add_mark(students[2], 77)

print(students)


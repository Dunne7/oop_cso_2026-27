#Complex Students
#instead of just being given their average we are given their results for the whole year
students = [
 {"name": "Evan", "marks": [65, 72, 81]},
 {"name": "Caleb", "marks": [45, 51, 48]},
 {"name": "Angelo", "marks": [82, 77, 91]},
 {"name": "Dorothy", "marks": [55, 63, 59]}
]

#Calculating averages

def calc_average(marks):
 return sum(marks) / len(marks)


# Test with several students
print(calc_average([60, 70, 80]))
print(calc_average([65, 72, 81]))
print(calc_average([45, 51, 48]))
print(calc_average([82, 77, 91]))
print(calc_average([55, 63, 59]))


# 1. Print each student's name and average
for student in students:
    average = calc_average(student["marks"])
    print(student["name"], average)

# 2. Print Caleb's average
print("Caleb's average:", calc_average(students[1]["marks"]))

#Exercise B3
for student in students:
    average = calc_average(student["marks"])

    if average >= 50:
        print(student["name"])

#Exercise B4
def add_mark(student_dict, new_mark):
 student_dict["marks"].append(new_mark)


# Add 66 to Caleb's marks
add_mark(students[1], 66)

print(students[1])



from people import Person

student_1 = Person()

if student_1.lhand == True:
    print(f"First Name: {student_1.fname}")
    print(f"Second Name: {student_1.sname}")
    print(f"Age: {student_1.age}")

else:
    print(f"First Name: {student_1.fname.upper()}")
    print(f"Second Name: {student_1.sname.upper()}")
    print(f"Age: {student_1.age}")






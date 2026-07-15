import numpy as np
dataType = [('name', 'S15'),('class', int), ('height', float)]
students = [('Arav', 6, 54.8), ("robin", 8, 34.1), ('Reba', 9, '34.5'),('Mattew', 4, '23.35')]
student_details = np.array(students,dtype=dataType)

print(students)
print(type(students))
print(np.sort(student_details, order="height"))
print(np.sort(student_details, order="class"))
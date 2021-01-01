
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

t_height = 0
for height in student_heights :
  t_height += height
print(f"The total height of the students is: {t_height}")

numb_students = 0
for students in student_heights :
  numb_students += 1
print(f"Their are {numb_students} students.")

average_height = t_height / numb_students
print(f"The average height of the students is: {round(average_height)}")

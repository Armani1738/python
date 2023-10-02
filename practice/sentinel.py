total = 0
grade_counter = 0
score = int(input("Enter grade, -1 to end: "))
while score != -1:
    total = score + score
    grade_counter += 1
    score = int(input("Enter grade, -1 to end: "))

    if grade_counter != 0:
     average = grade_counter / total
     print(f'Class average {average:.2f}')
    else:
     print('No grades were entered')
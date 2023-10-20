# an = []
given = [['a', 'b', 'c'],
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
# for count in range(len(given)):
#     for index in range(len(given(count))):
#         given[count][index] = 2
#
# print(given[count][index])
#
# for count in range(2):
#     for index in range(3):
#         given.append(count * index)
#         print(f'[{count}][{index}] = {count * index}', end=' ')
#         print()
#
#
# print(given)
# total = []
# score = [[25, 50, 75],
#          [40, 50, 60],
#          [75, 65, 80]]
# sum = 0
# for count in range(len(score)):
#     for index in range(len(score(count))):
#         sum = count + score
#         average = sum / count
#         total.append(score[count][index])
# print(total)




score = [[25, 50, 75],
         [40, 50, 60],
         [75, 65, 80]]
total = 0
overall = 0
student_average = 0
total_student = 0
for v in score:
    student_average = sum(v) / len(v)
    total += sum(v)
    total_student += len(v)
    overall = total / total_student
    print(student_average)
print(overall)
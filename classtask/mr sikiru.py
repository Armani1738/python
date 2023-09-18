# number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# odd = 0
# even = 0
#
# for count in number:
#     if count % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Number of even numbers:", even)
# print("Number of odd numbers:", odd)

even = 0
odd = 0
for number in range(1, 10):
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even number:", even)
print("Number of odd number:", odd)

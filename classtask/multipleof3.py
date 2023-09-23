# count = 1
# while count < 50:
#     if count % 15 == 0:
#         print("FizzBuzz")
#     elif count % 5 == 0:
#         print("Buzz")
#     elif count % 3 == 0:
#         print("Fizz")
#     else:
#         print(count)
#     count += 1
#
# print(count)

for count in range(1, 51):
    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    elif count %  5 == 0:
        print("Buzz")
    elif count % 3 == 0:
        print("Fizz")
    else:
        print(count)
        count += 1


# def largest_number(number):
#     number = "23569"
#     num = list(number)
#     count = 1
#     result = []
#     for i in range(5):
#         result = num[:count:]
#         highest = list(str(num))
#         if number > highest:
#             highest = result
#             result.append(highest)
#         count += 1
#     print(result)
#
#
# def highest_numbers(number):
#     largest = number[0]
#     for number in number:
#         if number > largest:
#             largest = number
#     return largest


def bigger_odds(numbers):
    return max([number for number in numbers if int(number) % 2 == 1])
# return list(filter(lambda  number: int (number) % 2 == 1, numbers))

# def armani(name, number=3):
#     return name * number
#
# print(armani(name= "Armani", number= 10))


def my_sum(*numbers):
    total = 0
    for i in numbers:
        total += i
        return total


print(sum([2, 3, 4, 6, 7, 8, 9, 1, 75]))

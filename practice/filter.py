import random
from string import ascii_letters, hexdigits
#
# numbers = [1, 10]
# count = 0
# result = filter(lambda number : count % 2 == 0, numbers)
#
# print(result)
numbers = list(range(0, 13))
numbers2 = list(range(0, 11))
letters = list(ascii_letters)
digits = list(hexdigits)
print(numbers)
print(numbers2)
print(letters)
print(digits)
print(list(zip(numbers, numbers2)))

result = list(filter(lambda n : n % 2 == 0, numbers))
print(result)

print(random.choice(letters))







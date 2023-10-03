def largest_element(number):
    largest = number[0]
    for number in number:
        if number > largest:
            largest = number
    return largest


def reverse_list(number):
    firstline = 0
    secondline = len(number) - 1
    while firstline < secondline:
        number = number[firstline]
        number[firstline] = number[secondline]
        number[secondline] = number
        firstline += 1
        secondline -= 1

    return number


def element(number, integer):
    for number in number:
        if number == integer:
            return True
    return False


def odd_number(number):
    odd = []
    for number in number[::2]:
        odd.append(number)
    return odd


def even_numbers(number):
    even = []
    for number in number[1::2]:
        even.append(number)
    return even


def sum1(number):
    sum = 0
    for number in range(0, len(number)):
        sum = sum + number[number]
    return sum


def sum_loop1(number):
    sum = 0
    count = 0
    while count < len(number):
        sum = sum + number[count]
        count += 1
    return sum

# my_array = "omo"
# print(palindrome(number))

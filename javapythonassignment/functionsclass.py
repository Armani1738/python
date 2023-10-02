def largest_element(array):
    largest = array[0]
    for number in array:
        if number > largest:
            largest = number
    return largest


def reverse_list(my_array):
    left_slide = 0
    right_side = len(my_array) - 1
    while left_slide < right_side:
        number = my_array[left_slide]
        my_array[left_slide] = my_array[right_side]
        my_array[right_side] = number
        left_slide += 1
        right_side -= 1

    return my_array

def check_element(my_array, to_check):
    for number in my_array:
        if number == to_check:
            return True
    return False


def odd_number(my_array):
    odd_position = []
    for number in range(1, len(my_array), 2):
        odd_position.append(my_array[number])
    return odd_position

def even_numbers(my_array):
    even_number = []
    for number in range(0, len(my_array), 2):
        even_number.append(my_array[number])
    return even_number

def sum_loop(my_array):
    sum = 0
    for number in range(0, len(my_array)):
        sum = sum + my_array[number]
    return sum

def sum_loop(my_array):
    sum =0
    count = 0
    while count < len(my_array):
        sum = sum + my_array[count]
        count += 1
    return sum

# my_array = "omo"
# print(palindrome(my_array))
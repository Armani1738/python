def list_of_numbers(first_number, second_number):
    numbers = []
    for number in range(first_number, second_number):
        numbers.append(number)
    return numbers


def odd(integers):
    odd_numbers_list = []
    for numbers in integers:
        if numbers % 2 == 1:
            odd_numbers_list.append(numbers)
    return odd_numbers_list


def double_item(lists):
    for numbers in range(len(lists)):
        lists[numbers] **= 2
    return lists


def change_element_index(lists):
    for index, nums in enumerate(lists):
        if 4 <= index <= 7:
            lists[index] = 0
    return lists


def empty_list(lists: list):
    lists.clear()
    return lists


def concatenate_list(first_list, second_list):
    lists = []
    for index in range(len(first_list)):
        strs = ""
        strs = first_list[index] + second_list[index]
        lists.append(strs)
    return lists
    

def excercise(list1, list2):
    return [x+y for x, y in zip(list1, list2)]



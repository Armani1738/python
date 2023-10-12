# names = ["john","james","joy","johnson"]
# names2 = list("john")
# tuple1 = 1,2,3
# tuple2 = 'a','b','c'
# list_to_tuple = tuple(names)
# print(list_to_tuple)
#
# tuple_to_list = list(list_to_tuple)
# print(tuple_to_list)
#
# print(names + names2)
#
# names[0] = "Armani"
# print(names)
#
# tuple3 = 1,2,3,"ope", ["udoh", "armani"], "Nehemiah"
# ans = tuple3[1] * 5
# print(ans)
# tuple3[4][0] = "Enimini"
# print(tuple3)
#
# lt = list(tuple3)
# lt[3] = "hoodboy"
# l = tuple(lt)
# print(l)
#
# a = (1, (1,2,3), ("a", "b"), 4, [5, 6], True)
# b = ["ijeh", "udoh", "armani", (1, 2), [3, 4], 10]
# b.pop()
# print(b)

# a, b, *c = names
# print(a, b, c)

# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# numbers *= 2
# print(numbers)
# # numbers.index(3, 5)
# # print(numbers.count(3))
# print(all(numbers))
# print(any(numbers))
#
# def my_index(li: list, number):
#     index = 0
#     for count in range(len(li)):
#         if li[count] == number:
#             index = count
#             break
#     return index
#
# print(my_index(numbers, 3))
#
# def my_sort_func(list1: list):
#     numbers = [1,2,3,4,5,66,7,8,9,10]
#     for count in range(len(numbers)):
#         if list1[count] == numbers:
#             break
#     return numbers

# List of Numbers
# numbers = []
# for count in range(1, 11):
#     numbers.append(count)
# print(numbers)
#
# numbers2 = [(range(1, 11))]
# print(numbers2)

def even_check(n):
    ans = 0
    if n % 2 == 0:
        ans = n
    return ans

my_numbers = [1,2,3,4,5,6,7,8,9,10]
even_list = filter(even_check, my_numbers)
print(list(even_list))

# another means to print

result =[count for count in range(1, 11) if count % 2 == 0]
print(result)

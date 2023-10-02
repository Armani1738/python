def divide_or_sqaure(number):
    if number * number % 5 == 0:
        return number ** number
    else:
         number % 5 == 1
    return number


print(divide_or_sqaure(15))

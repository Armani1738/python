import math

number = 10
userinput = int(input("Enter the number: "))
sum = number // userinput
print(sum)
def fibonacci(number):
    x = 0
    y = 1
    sum = x + y
    while x < 50:
        print(x, end=' ')
        x = y
        y = sum
        sum = x + y


fibonacci(50)



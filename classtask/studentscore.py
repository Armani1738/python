from random import random

count = 1
average = 0
total = 0
while count < 10:
    number = int(input("Enter your student number: "))
    total = total + number
    count += 1
average = total / count
print(average)


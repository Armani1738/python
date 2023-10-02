firstnumber = 0
number = 1
for count in range(0, 50):
    if count <= 50:
        number1 = firstnumber + number
    firstnumber, number = number,number1
    print(number1, end=' ')
number = 0
number1 = 1
sum = number + number1
while number < 50:
    print(number, end=' ')
    number = number1
    number1 = sum
    sum = number + number1

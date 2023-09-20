number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
number3 = int(input("Enter number3: "))

sum = number1 + number2 + number3
average = sum / 3
product = number1 * number2 * number3
print(sum)
print(average)
print(product)
if number1 > number2 and number1 > number3:
    print("the largest number is:",number1)
if number2 > number3 and number2 > number1:
    print("the largest number is:",number2)
if number3 > number1 and number3 > number2:
    print("the largest number is:",number3)
if number1 < number2 and number1 < number3:
    print("the smallest number is:", number1)
if number2 < number3 and number2 < number1:
    print("the smallest number is:", number2)
if number3 < number1 and number3 < number2:
    print("the smallest number is:", number3)

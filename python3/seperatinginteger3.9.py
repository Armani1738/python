five_numbers = int(input("Enter the number:"))
digit = five_numbers // 10000 % 10
digit1 = five_numbers // 1000 % 10
digit2 = five_numbers // 100 % 10
digit3 = five_numbers // 10 % 10
digit4 = five_numbers // 1 % 10

print(digit,digit1,digit2,digit3,digit4)
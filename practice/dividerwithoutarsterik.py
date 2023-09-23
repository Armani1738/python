numerator = int(input("Enter number you love to divide: "))
denominator = int(input("Enter number you love to divide with: "))
initial_holder = denominator
count = 0
while numerator >= denominator:

    denominator += initial_holder

    if denominator <= 0:
        print("Cannot divide by zero")
        break

    elif numerator == 0:
        print("0")
    count += 1
print(count)
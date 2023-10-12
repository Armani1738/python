def Calculators():
    userinput = int(input("""
        Choose an operation from the list:
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division """))
    firstnumber = int(input("Enter the first number: "))
    secondnumber = int(input("Enter the second number: "))
    if userinput == 1:
        print("Sum: {} + {} = {}".format(firstnumber, secondnumber, firstnumber + secondnumber))
    elif userinput == 2:
        print("Difference: {} - {} = {}".format(firstnumber, secondnumber, firstnumber - secondnumber))
    elif userinput == 3:
        print("Product: {} * {} = {}".format(firstnumber, secondnumber, firstnumber * secondnumber))
    elif userinput == 4:
        print("Divide: {} / {} = {}".format(firstnumber, secondnumber, firstnumber / secondnumber))
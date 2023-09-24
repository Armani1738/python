def userinput():
    userinput = int(input("Enter your investment: "))
    year = 0
    investment_amount = 10/100
    for count in range(1, 31):
        profit = userinput
        profit *= investment_amount
        userinput += profit
        print(f"your Roi is {profit:.2f} ,your investment is now ${userinput:.2f} in a year {count}")
        count += 1
range(userinput())
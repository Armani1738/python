
# row = 1 * 1
# column = 2 * 1
# for row in range(1, 13):
#     for column in range(2,  21):
#         print(f"{column} * {row  } = {row * column }", end='\t\t')
#     print()



# for row in range(1,  13):
#     for column in range(2,  21):
#         print(f"{column:>2} * {row:>2} = {row * column:>3}", end='\t\t')
#     print()

userinput = int(input("Enter your investment: "))
year = 0
investment_amount = 10/100
for count in range(1, 31):
    profit = userinput
    profit *= investment_amount
    userinput += profit
    print(f"your Roi is {profit:.2f} ,your investment is now ${userinput:.2f} in a year {count}")
    count += 1


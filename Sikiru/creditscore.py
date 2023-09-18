price = int(input("Enter item price: "))
credit_score = bool(input("Do you have a good credit score?if No ignore,if Yes type True: "))
item_name = input("Enter item name: ")
discount = 10
discount1 = 25

if credit_score:
    deposit = (discount * price) // 100

    print("******* Transaction successful *******")
    print(f'Your credit score is:{credit_score}\nYour item price is:{price}\n')
    print("***************************************")
    print("              Invoice                  ")
    print("***************************************")
    print("Name of item :", item_name)
    print(f"Discount(%):{discount} ")
    print(f"Deposit: {deposit}")
    print("***************************************")
    print("         Thanks For Patronage          ")
else:
    price2 = discount1 - price / 100
    deposit = 25 * price // 100
    print("****** insufficient credit score ******")
    print(f' your credit score is {credit_score} and your item price is {price}\n')
    print(f"**************************************")
    print("              Invoice                  ")
    print("***************************************")
    print("Name of item :", item_name)
    print(f"Discount (%): Not applied")
    print(f"Deposit {deposit}")
    print("***************************************")
    print("         Thanks For Patronage          ")
star = "*"
header1 = "Armani's & Sons Group of Company"
header2 = "312 Herbert Macauley Way, Sabo, Yaba"
header3 = "07018119827 primearmani@gmail.com"
star2 = "-"
product_ = []
quantity_ = []
price_ = []
total_ = []

for i in range(1, 5):
    product = input("Enter the product to be purchased: ")
    product_.append(product)

    quantity = int(input("Enter the quantity to be purchased: "))
    quantity_.append(quantity)

    price = int(input("Enter the price of the product: "))
    price_.append(price)

    total = quantity * price
    total_.append(total)

print(star * 80)
print("             " + header1)
print("             " + header2)
print("             " + header3)
print(star * 80)

print(star2 * 80)

print("             Product        quantity     price         total")
for i in range(0, 4):
    print(f"{product_[i]:>18}    {quantity_[i]:>9}     {price_[i]:>9}     {total_[i]:>9}")

print(star2 * 80)

print("                                                 Total: ", sum(total_))
print(star * 80)
print(star * 80)
print("                         ******* Thank You For Your Patronage ******")
print(star * 80)
print(star * 80)
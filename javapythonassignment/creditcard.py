
userinput = input("enter: ")
length =len(userinput)
print(length)
userinput1 = int(input("Hello, Kindly Enter Card details to verify: "))
mastercard = 5
visa_card = 4
American_Express_Card = 37
Discover_Card = 6
credits_card_type = (mastercard, visa_card, American_Express_Card, Discover_Card)

if userinput1:
    userinput1 = userinput1 >= 13 and userinput1 <= 16

    print("***************************************")
    print(f"**Credit Card Type: {credits_card_type}")
    print(f"**Credit Card Number: {userinput1}")
    print(f"**Credit Card Digit Length: {length}")
    print(f"Credit Card Validity Status: Valid")
    print("***************************************")
    print("         Thanks For Patronage          ")

else:
    userinput1 = userinput1 < 13 and userinput1 > 16

    print("***************************************")
    print(f"**Credit Card Type: {credits_card_type}")
    print(f"**Credit Card Number: {userinput1}")
    print(f"**Credit Card Digit Length: {length}")
    print(f"Credit Card Validity Status: Invalid")
    print("***************************************")
    print("   Please Enter a valid Credit card Number ")
    print("         Thanks For Patronage          ")
from javapythonassignment.creditcardfunctions import card_validity, card_type, length


userinput = input("Hello, Kindly Enter Card details to verify: ")
print("***************************************")
print(f"**Credit Card Type: {card_type(userinput)}")
print(f"**Credit Card Number: {userinput}")
print(f"**Credit Card Digit Length: {length(userinput)}")
print(f"**Credit Card Validity Status, {card_validity(userinput)}")
print("***************************************")

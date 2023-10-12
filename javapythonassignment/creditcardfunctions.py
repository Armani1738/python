def card_validity(userinput):
    if userinput > 13 and userinput < 16:
        print("Valid")
    elif userinput < 13 and userinput > 16:
        print("Invalid")

def card_type(userinput):
    if userinput[0] == 4:
        print("Visa Card")
    elif userinput[0] == 5:
        print("MasterCard")
    elif userinput[0] == 3 and userinput[1] == 7:
        print("American Express Card")
    elif userinput[0] == 6:
        print("Discovery Card")
    else:
        print("Unrecognize input")

def length(userinput):
    length = len(userinput)
    print(length)

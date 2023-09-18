import random
guess_number = random.randint(1, 10)
usernumber = int(input("Enter your number:"))
while usernumber != guess_number:
    usernumber = int(input("Enter your number:"))
    if usernumber == guess_number :
        print("congratulation", usernumber, "is the correct number")
    else :
        print("The number",usernumber , "wrong number")

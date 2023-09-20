numberone = int(input("Enter the number: "))
numbertwo = int(input("Enter the number: "))
numberthree = int(input("Enter the number: "))
sum = numberone + numbertwo + numberthree
average = sum / 3
product = numberone * numbertwo * numberthree

if numberone > numbertwo and numberone > numberthree:
    maximium = numberone
elif numbertwo > numberone and numbertwo > numberthree:
    maximium = numbertwo
elif numberthree > numberone and numberthree > numbertwo:
    maximium = numberthree
if numberone < numbertwo and numberone < numberthree:
    minimium = numberone
elif numbertwo < numberone and numbertwo < numberthree:
    minimium = numbertwo
elif numberthree < numberone and numberthree < numbertwo:
    minimium = numberthree

print("The sum of the numbers:",sum,"\nThe average of the number is:",average,"\nThe product of the numbers:",product)
print("The maximium of the number is:", maximium,"\nThe minimium of the number is:", minimium)


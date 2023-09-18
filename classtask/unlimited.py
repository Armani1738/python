unlimited = int(input("Enter your student number: "))
total = 0
count = 1
while unlimited != 0:
    unlimited = int(input("Enter your student number: "))
    count += 1
    total = total + unlimited
average = total / count
print(average)
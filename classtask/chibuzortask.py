sum = 0
count = 1
average = 0
total = 0
for num in range (1, 11):
    number = int(input("Enter your student number: "))
    total = total + number
    count += 1
average = total / count
print("The total score is:", total)
print("The average score is: ",average)
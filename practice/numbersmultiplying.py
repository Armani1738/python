ls = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
for i in range(0, len(ls)):
    for j in range(i + 1, len(ls)):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]

print(ls)
l = len(ls)

if l % 2 == 0:
    m1 = ls [l // 2]
    m2 = ls [l // 2]
    mid = (m1 + m2) / 2

    print(mid)
ls = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
mean_ls = sum(ls) / len(ls)

print(mean_ls)
mean = 0
ls = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
for j in ls:
    mean += j
mean = mean / mean
print(mean)



number = [5,20,15,20 ,30 ,40,15,75,3,9]
for a in range(0, len(number)):
    for b in range(a + 1, len(number)):
        if number[a] > number [b]:
            number[a], number[b] = number[b], number[a]

print(number)

number = [7,3,6,0,49,50,100,21,201]
for taye in range(0, len(number)):
    for kehinde in range(taye + 1, len(number)):
        if number[taye] > number[kehinde]:
            number[taye], number[kehinde] = number[kehinde], number[taye]

print(number)

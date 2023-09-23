
number = 5
for row in range(6):
    print()
    for column in range(row-1):
        print('*', end=' ')
for rows in range(6):
    print()
    for column in range(3-rows):
        print('* ', end='')

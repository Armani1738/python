def shape(number):
    for row in range(number):
        print()
        for column in range(row - 1):
            print('*', end=' ')
    for rows in range(number):

        print()
        for column in range(3 - rows):
            print('* ', end='')

shape(6)
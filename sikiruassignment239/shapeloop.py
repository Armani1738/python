def shape(number):
    for row in number:
        print()
        for column in range(row - 1):
            print('*', end=' ')
    for rows in number:

        print()
        for column in range(3 - rows):
            print('* ', end='')

shape(range(6))
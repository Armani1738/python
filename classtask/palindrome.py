def is_palindrome(number):
    for a in range(number):
        for b in range(a, number):
            print(' ', end=' ')
        for b in range(a + 1):
            print("*", end=' ')
        for b in range(a):
            print('*', end=' ')
        print()


is_palindrome(5)

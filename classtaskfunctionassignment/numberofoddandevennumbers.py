def number(range):
    even = 0
    odd = 0
    for number in range(1, 10):
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Number of even number:", even)
    print("Number of odd number:", odd)
number(range)
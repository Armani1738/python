def reverse(tuples):
    new_tuple = ()
    for number in range(len(tuples)):
        new_tuple0 = tuples[(number - 0)]
        new_tuple1 = tuples[(number - 1)]
        new_tuple2 = tuples[(number - 2)]
        new_tuple3 = tuples[(number - 3)]
        new_tuple4 = tuples[(number - 4)]
        new_tuple = new_tuple0, new_tuple1, new_tuple2, new_tuple3, new_tuple4
    return new_tuple


def nested_tuple(numbers):
    number = []
    for count in range(len(numbers)):
        for count in range (count +1, len(numbers)):
            firstnumber = numbers [0][1]
            secondnumber = numbers [1][2]
            number = ((firstnumber), (secondnumber))
    return number


def last_and_first_number(numbers):
    lastnfirst = ()
    for count in range(len(numbers)):
        firstnumber = numbers[-1]
        secondnumber = numbers[0]
        lastnfirst = firstnumber, secondnumber
    return lastnfirst


def sorted_numbers(numbers):
    sorted = ()
    for count in range(len(numbers)):
        firstnumber = numbers [0]
        secondnumber = numbers [1]
        thirdnumber = numbers [2]
        forthnumber = numbers [3]
        sorted = ((thirdnumber, firstnumber),(forthnumber, secondnumber))
    return sorted


def appeared_numbers(numbers):
    number = []
    for count in range(len(numbers)):
        for counts in range (count +1, len(numbers)):
            if numbers[count] == numbers[counts] and numbers[count] not in number:
                number.append(numbers[count])
    return number

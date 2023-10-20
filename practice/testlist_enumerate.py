test_list = [
    [0, 0, 0],
    [0, 0, 0]
]
test_list[0][0] = 5
test_list[0][1] = 5
test_list[0][2] = 5
test_list[0][0] = 5
test_list[1][1] = 5
test_list[1][2] = 5
for i in enumerate(test_list):

    for i, val in enumerate(test_list):
        for j, _ in enumerate(val):
            result = test_list[i][j] = 5

print(test_list)
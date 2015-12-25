def keygen(row, col):
    rounds = sum(range(row + col - 1)) + col
    code = 20151125
    for i in range(1, rounds):
        code = code * 252533 % 33554393

    print(code)
    return code

keygen(2978, 3083)

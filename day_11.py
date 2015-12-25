from string import ascii_lowercase

secure_letters = [a for a in ascii_lowercase if a not in {'i', 'o', 'l'}]
three_sequential = list(map(''.join, zip(secure_letters, secure_letters[1:], secure_letters[2:])))
pairs = [a + a for a in secure_letters]


def elf_security(password):
    check_a = any(three in password for three in three_sequential)
    check_b = sum(pair in password for pair in pairs) >= 2

    return check_a and check_b


def cycle_password(password):
    index = [secure_letters.index(x) for x in password]

    i = len(index) - 1
    while i >= 0:
        if index[i] == 22:  # as we removed three letters
            index[i] = 0
            i -= 1
        else:
            index[i] += 1
            break

    password = ''.join(secure_letters[i] for i in index)

    return password


p = 'hepxcrrq'

while True:
    p = cycle_password(p)
    if elf_security(p):
        break

print(p)

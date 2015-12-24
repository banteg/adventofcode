from click import progressbar
from numpy import zeros, arange, nonzero

limit = 36000000


def deliver_presents():
    one = zeros(limit // 10, dtype=int)
    two = zeros(limit // 10, dtype=int)
    with progressbar(arange(1, limit // 10)) as bar:
        for elf in bar:
            one[elf::elf] += elf * 10
            two[elf:elf * 50 + 1:elf] += elf * 11

    result_one = nonzero(one >= limit)[0][0]
    result_two = nonzero(two >= limit)[0][0]
    print(result_one)
    print(result_two)


deliver_presents()

from click import progressbar
from numpy import zeros, arange

limit = 36000000


def deliver_presents(limited=False):
    hood = zeros(limit // 10, dtype=int)
    with progressbar(arange(1, limit // 10)) as bar:
        for elf in bar:
            if limited:
                hood[elf:elf * 50 + 1:elf] += elf * 11
            else:
                hood[elf::elf] += elf * 10

    cond = ((k, v) for k, v in enumerate(hood) if v >= limit)
    result = min(cond)
    print(result)
    return result


deliver_presents()
deliver_presents(limited=True)

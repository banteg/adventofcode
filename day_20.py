from click import progressbar
from numpy import zeros, arange

limit = 36000000
hood = zeros(limit // 10)


def deliver_presents():
    with progressbar(arange(1, limit // 10)) as bar:
        for elf in bar:
            hood[elf::elf] += elf * 10


deliver_presents()
cond = ((k, v) for k, v in enumerate(hood) if v >= limit)
result = min(cond)
print(result)

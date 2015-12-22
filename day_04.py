'''
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle input is yzbqklnj.

--- Part Two ---

Now find one that starts with six zeroes.
'''


from hashlib import md5


def miner(secret, zeros=5):
    c = 1
    while True:
        s = '{secret}{c}'.format_map(locals()).encode('u8')
        if md5(s).hexdigest().startswith('0' * zeros):
            return c
        c += 1


def tests():
    assert miner('abcdef') == 609043
    assert miner('pqrstuv') == 1048970


tests()
coins = miner('yzbqklnj')
print(coins)

more_coins = miner('yzbqklnj', zeros=6)
print(more_coins)

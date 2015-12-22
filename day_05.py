'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
'''

import re


def is_nice(s):
    vovels = re.findall(r'[aeiou]', s)
    twice = re.findall(r'(.)\1', s)
    bad = re.findall(r'(ab|cd|pq|xy)', s)
    return bool(len(vovels) >= 3 and twice and not bad)


def test():
    assert is_nice('ugknbfddgicrmopn') == True
    assert is_nice('aaa') == True
    assert is_nice('jchzalrnumimnmhp') == False
    assert is_nice('haegwjzuvuyypxyu') == False
    assert is_nice('dvszwmarrgswjxmb') == False


def find_out_nice(file):
    with open(file) as f:
        inputs = f.readlines()

    result = sum(map(is_nice, inputs))
    print(result)


test()
find_out_nice('inputs/day_05.txt')

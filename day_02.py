'''
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
'''
def wrap_present(size):
    l, w, h = size
    sides = l * w, w * h, h * l
    paper = 2 * sum(sides) + min(sides)
    return paper


def tests():
    assert wrap_present((2, 3, 4)) == 58
    assert wrap_present((1, 1, 10)) == 43


def order_paper(file):
    parse_size = lambda x: tuple(map(int, x.strip().split('x')))
    with open(file) as f:
        presents = [parse_size(x) for x in f]

    order = sum(map(wrap_present, presents))
    print(order)
    return order


tests()
order_paper('inputs/day_02.txt')

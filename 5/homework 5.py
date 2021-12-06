d = [1, 2, 3, 4, 5, 6, 7]
def search(d, n):
    lower = -1
    upper = len(d) - 1
    while lower < upper - 1:
        center = (lower + upper) // 2
        if d[center] >= n:
            upper = center
        else:
            lower = center
    if upper >= 0 and d[upper] == n:
        return upper
    else:
        return None
n = int(input("Введите искомый элемент:"))


print(search(d, n))
assert search([], 42) is None
assert search([0], 0) == 0
assert search([0], 1) is None
assert search([-1, 0, 42], 0) == 1
assert search([-42, 0, 42], 42) == 2
assert search([-6, -5, -4, -3, -2, -1], -4) == 2
assert search([1, 2, 3, 4, 5, 6], 4) == 3
assert search([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert search([1, 2, 3, 4, 5], 7) is None
assert search([1, 2, 3, 4, 5, 6], 7) is None
assert search([42, 42, 42, 42, 42], 42) == 0
assert search([-42, -42, -42, -42, -42], -42) == 0
assert search([42, 42, 42, 42, 43], 43) == 4
assert search([41, 42, 42, 42, 42], 41) == 0
assert search([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
assert search([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4

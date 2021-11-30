d = [1, 2, 3, 4, 5, 6, 7]
def search(d, n):
    lower = 0
    upper = len(d) - 1
    while lower <= upper:
        center = (lower + upper) // 2
        if d[center] == n:
            return center
        elif d[center] > n:
            upper = center - 1
        elif d[center] < n:
            lower = center + 1
    return None
n = int(input("Введите искомый элемент:"))


print(search(d, n))
assert search([], 4) == None
assert search([1, 2, 3, 4, 5, 6, 7], 1) == 0
assert search([1, 2, 3, 4, 5, 6, 7], 0) == None
assert search([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert search([1, 2, 2, 4, 5, 6, 7], 2) == 1

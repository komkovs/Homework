d = [1, 9, 2, 8, 3, 7, 4, 6, 5]
d = sorted(d)
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


n = int(input("Искомый элемент: "))
print(search(d, n))
assert search([], 4) == None
assert search([1, 9, 2, 8, 3, 7, 4, 6, 5], 1) == 0
assert search([1, 9, 2, 8, 3, 7, 4, 6, 5], 0) == None
assert search([1, 9, 2, 8, 3, 7, 4, 6, 5], 4) == 3
assert search([1, 2, 2, 8, 3, 7, 4, 6, 5], 2) == 1

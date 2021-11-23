def function():
    f = input("Введите элементы списка\n")
    b = list()
    while f != "":
        b.append(f)
        f = input()
    k = int(input("Введите k\n"))
    b = b[-k:] + b[:-k]
    return b
print(function())

def function():
    assert function([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
    assert function([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert function([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
    assert function([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert function([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]

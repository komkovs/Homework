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

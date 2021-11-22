def function():
    try:
        f = input("Введите элементы списка\n")
        b = list()
        while f != "":
            b.append(f)
            f = input()
        assert b != []
        k = int(input("Введите k\n"))
        b = b[-k:] + b[:-k]
        return b
    except AssertionError:
        return "Долбан"
print(function())

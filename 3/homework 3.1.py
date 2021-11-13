def function():
    f = input()
    b = list()
    while f != '':
        b.append(f)
        f = input()
    return b

print(function())
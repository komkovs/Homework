def function():
    f = input()
    b = list()
    while f != '':
        b.append(f)
        f = input()
    if len(b) == len(set(b)):
        print("t")
    else:
        print("f")
print(function())
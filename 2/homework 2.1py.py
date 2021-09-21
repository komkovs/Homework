x = str(input("Введите что-нибудь"))
b = list()
while x != '':
    x = str(input())
    b.append(x)
else:
    del b[len(b)-1]
    print(b)
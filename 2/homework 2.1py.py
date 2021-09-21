x = str(input("Введите что-нибудь"))
b = list()
while x != '':
    b.append(x)
    x = str(input())
else:
    print(b)
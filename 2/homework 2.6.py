z = []
l = input()
k = int(input())
for i in l:
    if i.isdigit():
        z.append(i)
print(z[k - 1])

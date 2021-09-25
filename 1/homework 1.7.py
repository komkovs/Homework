m = 0
x = int(input())
y = int(input())
for i in range(x, y+1):
    if i % 5 == 0:
        m += i
print(m)

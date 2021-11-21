def function(b):
    x = sum(b) / len(b)
    print(x)
b = list()
n = input()
while n != '':
    b.append(float(n))
    n = input()
function(b)
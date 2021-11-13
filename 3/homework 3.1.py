def function(x):
    b = list()
    while x != '':
        b.append(x)
        x = input()
    return(b)

f = input()
print(function(f))
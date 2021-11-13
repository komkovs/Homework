def function(x):
    t1, t2 = 0, 1
    while x > 0:
        print(t1, end = " ")
        t1, t2 = t2, t1 + t2
        x = x - 1

n = int(input())
function(n)
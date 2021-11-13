def function(x):
    t1, t2 = 0, 1
    for _ in range(x):
        print(t1, end = " ")
        t1, t2 = t2, t1 + t2

n = int(input())
function(n)
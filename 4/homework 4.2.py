def function():
    n = int(input("Введите n"))
    if n == 0:
        return 1
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial 
print(function())

def function():
    assert function(3) == 6
    assert function(0) == 1


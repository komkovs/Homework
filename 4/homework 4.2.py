def function():
    n = int(input("Введите n:\n"))
    try:
        assert n > -1
        if n == 0:
            return 1
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return factorial
    except AssertionError:
        return "Не вводи отрицательное" 
print(function())
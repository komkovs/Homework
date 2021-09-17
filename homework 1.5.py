x = int(input("Введите X"))
y = int(input("Введите Y"))
if x>0 and y>0:
    print("1 четверть")
if x<0 and y>0:
    print("2 четверть")
if x<0 and y<0:
    print("3 четверть")
if x>0 and y<0:
    print("4 четверть")
if x==0 or y==0:
    print("Точка лежит на оси")

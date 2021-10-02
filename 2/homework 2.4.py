n = input()
z = n.count("(")
t = n.count(")")
if z > t:
    print("Не хватает закрывающей", z - t)
elif z < t:
    print ("Не хватает открывающей", t - z)
else: 
    print("Все норм")
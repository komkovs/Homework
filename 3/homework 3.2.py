def time(x):
    if x == 12 or x == 1 or x == 2:
        return"зима"
    elif x > 12 or x < 0:
        return"серьезно?"
    elif x > 2 and x < 6:
        return"весна"
    elif x > 5 and x <9 :
        return"лето"
    else:
        return"осень"

f = int(input())
print(time(f))
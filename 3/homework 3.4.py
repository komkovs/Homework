from homework import function
def f1(b):
    print("\tЭлемент","|", "\tЧастота")
    for x in set(b):
        y = b.count(x)
        print("\t", x, "\t|", "\t", y)
b = function()
f1(b)
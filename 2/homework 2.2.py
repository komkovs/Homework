i = input()
i = i.replace(" ","")
s = list(i)
n = list()
for l in range(0,len(s)):
    n.append(int(s[l]))
n.sort()
n.reverse()
v = str()
for l in range(0,len(n)):
    v=v+str(n[l])
print(v)
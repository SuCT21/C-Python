x=input()
d=0;
for i in range(0,len(x)):
    weight=8**(len(x)-i-1)
    d=d+weight
print(d)

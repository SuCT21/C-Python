b=input()
d=0;
for i in range(0,len(b)):
    if b[i]=='1':
        weight=(0.5)**(len(b)-i)
        d=d+weight
print(d)

b=input()
d=0;
for i in range(0,len(b)):
    if b[i]=='1':
#如果i取1时再进行计算
        weight=2**(len(b)-i-1)
        d=d+weight
print(d)
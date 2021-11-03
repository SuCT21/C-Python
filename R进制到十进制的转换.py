a=int(input("要进行转换的进制："))
R=input()
d=0;weight=0
for i in range(0,len(R)):
    if R[i]!='0':
        weight=(int(R[i]))*(a**(len(R)-1-i))
        d=d+weight
print(d)
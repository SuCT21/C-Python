b=[]
def toTen(x):
    total = 0
    for i in range(len(x)):
        if x[i] >= '0' and x[i] <= '9':
            total+=(int(x[i])) * (n ** i)
        elif x[i] >= 'A' and x[i] <= 'Z':
            #print(ord(x[i])-ord('A')+10)
            total+=(ord(x[i])-ord('A')+10) * (n ** i)
    return total
def toM(x):
    while x > 0:
        b.append(x % m)
        x = x // m
n = int(input("请输入需要转换的进制数："))
a = str(input("请输入该进制数"))
m = int(input("请输入转换后的进制数："))
a = a[::-1]
toM(toTen(a))
b.reverse()
for i in range(len(b)):
    if b[i]>=10:
        print(chr(b[i]-10+ord('A')),end='')
    else:
        print(b[i],end='')

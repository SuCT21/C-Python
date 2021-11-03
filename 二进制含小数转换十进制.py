print("请输入只包括0，1和小数点组成的字符串")
dot_num=0
dot_position=0
b=input()
c=0;d=0;
for i in range(0,len(b)):
    if b[i]!='0' and b[i]!='1' and b[i]!='.':
        print("输入错误，请重新输入")
        break
(x,t,y)=b.partition('.')
for i1 in range(0,len(x)):
    if x[i1]=='1':
        weight1=2**(len(x)-i1-1)
        c=c+weight1
for i2 in range(0,len(y)):
    if y[i2]=='1':
        weight2=(0.5)**(len(y)-i2)
        d=d+weight2
print(c+d)
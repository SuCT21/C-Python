b=input()
(x,t,y)=b.partition('.')
d1=0;d2=0;weight1=0;weight2=0;
weight1=2**(len(x)-1)
weight2=(0.5)**(len(y))
for i1 in range(0,len(x)):
    if x[i1]=='1':
        d1=d1+weight1
    weight1=weight1//2
for i2 in  range(0,len(y)): 
    if y[i2]=='1':
        d2=d2+weight2
    weight2=weight2//0.5
print(d1+d2)

b=input()
d=0;weight=2**(len(b)-1);
#weight=2^n-1
for i in range(0,len(b)):
    if b[i]=='1':
#二进制数都是由1和0组成，取到1时再进行计算，0计算后结果还是0
        d=d+weight;
    weight=weight//2;
#weight//2相当与2^n-2,2^n-3………2^2,2^1,2^0
print(d)
x=int(input())
r=0;
Rs=[];
while(x != 0):
    r=x%2
    x=x//2
    Rs=[r]+Rs
for i in range(0,len(Rs)):
    print(Rs[i],end='')
#进制计算取结果时，最后一个求余的结果是最高位
'''
r=x%2,%求余，//整数除
x=x//2
'''

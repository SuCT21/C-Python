x=int(input())
r=0;
Rs=[];
while(x!=0):
    r=x%8
    x=x//8
    Rs=[r]+Rs
for i in range(0,len(Rs)):
    print(Rs[i],end='')

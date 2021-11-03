b=input()
(x,t,y)=b.partition('.')
n=0;m=0;
rs1=[];rs2=[];
while(b!='0'):
    n=x%2
    x=x//2
    rs1=[n]+rs1
    m=y%2
    y=y//2
    rs2=[n]+rs2
for i1 in range(0,len(rs1)):
    print(rs1[i1])
for i2 in range(0,len(rs2)):
    print(rs2[i2],end='')
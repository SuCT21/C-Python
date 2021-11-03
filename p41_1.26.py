raw=[]
for i in range(4):
    x=int(input('第%d个数：'%i))
    raw.append(x)#.append,在raw这个数组里加入变量
for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]<raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print('四个数从大到小排列如下：%s'%raw)
#引导符，引导输出、输入的数据类型，%d：数字类 %f：带小数点的数字类 %c：字母、符号类 %s：数组、字符串类

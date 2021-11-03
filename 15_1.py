#计算阶乘
n=15
if n == 0:
    print(1)
else:
    res = 1
    for i in range(1,n+1):
        res = res*i
    print(res)
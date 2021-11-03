#求(x+1)^n的展开式
def combination(n,k):
    if k<0 or n<=0 or k>n:
        print("error")
    elif k ==0:
            print(1)
    else:
        X=1
        Y=1
        for i in range(n-k+1,n+1):
            X=X*i
        for j in range(1,k+1):
            Y=Y*j
        print(X/Y,"X^",k)
#C(n,k)=n!\(k!*(n-k)!)=n(n-1)...(n-k+1)\k!
#""里面是放的是要一直输出的东西，然后用，来连接要输出的数据
combination(10,0)
combination(10,1)
combination(10,2)
combination(10,3)
combination(10,4)
combination(10,5)
combination(10,6)
combination(10,7)
combination(10,8)
combination(10,9)
combination(10,10)


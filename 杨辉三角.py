def init(x):
    temp = int(x)
    def factor(x):
        if x >=1:
            return x*factor(x-1)
        else:
            return 1
        
    a=factor(x)
    
    for i in range(x+1):
        b=factor(i)
        c=factor(x-i)
        d=int(a / (b*c))
        if(temp!=0):
            if d ==1:
                print("x^{0}+".format(temp),end="")
            else:
                print("{0}x^{1}+".format(d,temp),end="")
        else:
            print("1",end="")
        temp-=1
intput=int(input("请输入次方数"))
init(input)

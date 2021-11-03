def factor(n):
    if n < 0:
        print("error")
    elif n == 0:
        print(1)
    else:
        res = 1
        for i in range(1,n+1):
            res = res*i
        return(res)
factor(4)
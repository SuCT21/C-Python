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
        print(X/Y)
combination(10,4)
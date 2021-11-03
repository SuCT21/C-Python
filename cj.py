#a = int (input("请输入一个数："))
while True:
    ten=input("")
    try:
        a=eval(ten)
        if type(a)==float or type(a)==int:
            break
    except:
        pass
if a >=90 and a<=100:
    print("优秀")
if a>=80 and a<=89:
    print("良")
if a>=70 and a<=79:
    print("中")
if a>=60 and a<=69:
    print("及格")
if a<60:
    print("不及格")
if a>100:
    print("error")
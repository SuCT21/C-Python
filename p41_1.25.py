w = int(input("请输入一个数："))
x = int(input("请输入一个数："))
y = int(input("请输入一个数："))
z = int(input("请输入一个数："))
if w>x and x>y and y>z:
    print(w,x,y,z)
if w>x and x>z and z>y:
    print(w,x,z,y)
if w>y and y>z and z>x:
    print(w,y,z,x)
if w>y and y>x and x>z:
    print(w,y,x,z)
if w>z and z>y and y>x:
    print(w,z,y,x)
if w>z and z>x and x>y:
    print(w,z,x,y)
if x>w and w>y and y>z:
    print(x,w,y,z)
if x>w and w>z and z>y:
    print(x,w,z,y)
if x>y and y>w and w>z:
    print(x,y,w,z)
if x>y and y>z and z>w:
    print(x,y,z,w)
if x>z and z>y and y>w:
    print(x,z,y,w)
if x>z and z>w and w>y:
    print(x,z,w,y)
if y>w and w>x and x>z:
    print(y,w,x,z)
if y>w and w>z and z>x:
    print(y,w,z,x)
if y>x and x>w and w>z:
    print(y,x,w,z)
if y>x and x>z and z>w:
    print(y,x,z,w)
if y>z and z>x and x>w:
    print(y,z,x,w)
if y>z and z>w and w>x:
    print(y,z,w,x)
if z>w and w>x and x>y:
    print(z,w,x,y)
if z>w and w>y and y>x:
    print(z,w,y,x)
if z>x and x>y and y>w:
    print(z,x,y,w)
if z>x and x>w and w>y:
    print(z,x,w,y)
if z>y and y>x and x>w:
    print(z,y,x,w)
if z>y and y>w and w>x:
    print(z,y,w,x)


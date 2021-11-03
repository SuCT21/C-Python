# r=25
# area=3.1415*r*r
# print(area)
# print("{:.2f}".format(area))
#画同心圆
# import turtle
# turtle.pensize(2)
# turtle.circle(10)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(100)
#画五角星
from turtle import *
color('red','red')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill
done()
# n=int (input())
# q=int(input())
# p=int(input())
# for q,p in range(1,n):
#     A=30+q,B=30+p
# if A<=0:
#     print(A,B,"Bob")
# if B<=0:
#     print(A,B,"Alice")
# if A>0 and B>0:
#     print("Draw")
i = int(input())
if i%4==0 and i%100!=0 and i%400==0:
    print("1")
else:
    print("0")

letter=str(input())
li=[]
for i in letter:
    li.append(i)
n=len(li)
first=li[0]
capital=first.upper()
li[0]=capital
for _ in range(0,n):
    print(li[_], end="")
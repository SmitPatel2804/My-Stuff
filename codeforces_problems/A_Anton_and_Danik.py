n=int(input())
string=str(input())
list=[]
for i in string:
    list.append(i)

x=list.count("A")
y=list.count("D")
if(x>y):
    print("Anton")
elif(x<y):
    print("Danik")
else:
    print("Friendship")
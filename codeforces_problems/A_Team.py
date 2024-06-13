n=int(input())
li_ques=[]
for _ in range(n):
    inp=str(input())
    li_ques.append(inp)
z=len(li_ques)-1
li=[]
for l in range(0,z):
    for string in li_ques:
        for i in string:
            li[l]=i
print(li)
            
    


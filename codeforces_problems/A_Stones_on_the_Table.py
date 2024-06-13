n=int(input())
letter=str(input())
li=[]
lii=[]
for l in letter:
    li.append(l)
    i=len(li)-1
for l in range(0,i):
    if(li[l]==li[l+1]):
        lii.append(1)
print(len(lii))
    

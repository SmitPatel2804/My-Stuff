n=int(input())
li=[]
X=0
if(n>=1 and n<=150):
    for _ in range(n):
        line=str(input())
        li.append(line)
    for i in li:
        if(i=="X++" or i=="++X"):
            X=X+1
            
        if(i=="X--" or i=="--X"):
            X=X-1
    print(X)
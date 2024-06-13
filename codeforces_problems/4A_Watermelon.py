w=int(input())
l=[]
if(w>=1 and w<=100):
    for i in range(w+1):
        if(i!=0):
            b=w-i
            if(b!=0):
                if(i%2==0 and b%2==0):
                    l.append("YES")
                else:
                    l.append("NO")
            else:
                continue
        else:
            continue
    if(l.count("YES")>=1):
        print("YES")
    else:
        print("NO")

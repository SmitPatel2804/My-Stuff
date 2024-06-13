n=int(input())
lines=[]
for no in range(n):
    line=str(input())
    lines.append(line)
for line in lines:
    if(len(line)<=10):
        print(line.lower())
    else:
        line=line.lower()
        list=[]
        for char in line:
            list.append(char)
        result=f"{list[0]}{len(line)-2}{list[-1]}"
        print(result)





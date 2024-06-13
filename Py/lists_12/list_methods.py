l=[1,3,12,4,5,10,7,8,9,2,1]
print(l)
l.append(11)
print(l)
l.sort() #ascending
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(12))
print(l.count(1))
m=l
m[0]=0
print(l)
print(m)
print(type(m))
 
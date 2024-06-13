l=[3,5,6]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
#list are changable
list1=["smit",5,2,"patel",5,6,7,8]
print(list1[0])
#using negative index
print(list1[0])
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
if 1 in list1:
    print("yes")
else:
    print("No")

print(list1[1:-1])
print(list1[1:5:2]) #1st index to 4th index and with difference 2

lst=[i*i for i in range(4) if i%2==0]
print(lst)
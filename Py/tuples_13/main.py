# tuple cannot be altered
tup = (1,5,6)
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])

if 5 in tup:
    print("Yes")
tup2=tup[0:]
print(tup2)
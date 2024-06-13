#difference between for loop and while loop
for i in range(0,5):
    print(i)

a=0
while(a<5):
    print(a)
    a += 1

#note: there is difference in += and =+
# a = 5
# a=+2
# logic : a = 2
# output : 2

# a = 5
# a+=2
# logic: a = a + 2
# output : 7

#decrementing loop
p=5
while(p>0):
    print(p)
    p-=1

#Else with while loop
q=5
while(q>0):
    print(q)
    q-=1
else:
    print("You are done with loop.")
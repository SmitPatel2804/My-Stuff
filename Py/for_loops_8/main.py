#for loop can iterate over illerable objects in python.
#example
name = "Smit"
for i in name:
    print(i, end=" ")
print("\n")

#using list
list = ["red", "blue", "yellow"]
for color in list:
    print(color.title(),"\n")

#use of range
for k in range(0,11):
    print(k)

#use of step in for loops
for o in range(1,12,3):
    print(o)
#here 3 will be the difference between each term in 1 to 12.
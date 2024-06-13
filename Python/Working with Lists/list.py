#Looping Through an Entire List
#. When you want to do the same action with every item in a list, you can use Python’s for loop.
cars=['hyundai','suzuki','tata','toyota']
for car in cars:
    print(car.title())
#here, all names are stored in a variable named car
    
#A Closer Look at Looping
#In for loop, python retrieve the first value from the list or item(specified in list) and keeps storing the string in the variable and repeats the same for second value and next..

#Doing More Work Within a for Loop
for car in cars:
    print(car.title()+" is a good car"+".\n")
#Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list. Therefore, you can do as much work as you like with each value in the list.
for car in cars:
    print(car.title()+" is a good car.")
    print("I want to buy "+car.title()+".\n")

print("Thank you for you time.")
#because the above line is not indented, it’s printed only once.
#note: Always indent the line after the for statement in a loop. If you forget, Python will remind you.

#Making Numerical Lists

#Using the range() Function
#Python’s range() function makes it easy to generate a series of numbers. 
for value in range(1,6):
    print(value)

#Using range() to Make a List of Numbers
numbers=list(range(1,6))
print(numbers)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
    print(squares)
#this will print after taking one one values from the range.
# for printing a normal list, print it outside for loop
print(squares)

#Simple Statistics with a List of Numbers
digits=list(range(1,11))
print(digits)
print(max(digits))
print(min(digits))
print(sum(digits))

#List Comprehensions
#A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
sq=[val**2 for val in range(1,11)]
print(sq)

#Working with Part of a List
#Slicing a List
players=['smit','mihir','dhruv','prince']
titled_players=[player.title() for player in players]
print(titled_players)

#Looping Through a Slice
for player in players[1:5]:
    print(player.title())
#this will print individual named of all players in the list with titled.

#Copying a List
#To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). 
myfood=['pizza','aloo paratha','sandwich','dhosa']
friendfood=myfood[:]
print("My favourite food is:")
foodmy=[titledmyfood.title() for titledmyfood in myfood]
foodfriend=[titledfriendfood.title() for titledfriendfood in friendfood]
print(foodmy)
print("\nMy friend's favourite food is:")
print(foodfriend)
foodmy.append('takos')
foodfriend.append('jalebi')
foodmy2=[titledmyfood.title() for titledmyfood in foodmy]
foodfriend2=[titledfriendfood.title() for titledfriendfood in foodfriend]
print("My favourite food is:")
print(foodmy2)
print("\nMy friend's favourite food is:")
print(foodfriend2)

#Tuples
#A tuple looks just like a list except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
print(dimensions[0:])

#Looping Through All Values in a Tuple
print('original dimensions'.title())
for dimension in dimensions:
    print(dimension)

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
listdimension=list(dimensions)
listdimension[0]=400
listdimension[1]=55
dimensions=tuple(listdimension)
print(dimensions)
print("\nnew dimensions".title())
for dimension in dimensions:
    print(dimension)












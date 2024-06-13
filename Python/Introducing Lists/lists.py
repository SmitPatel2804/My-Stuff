cars=['audi','mercedes','volvo','rolls-royce']
print(cars)

#accessing the lists
print(cars[0].title())

#Using Individual Values from a List
msg1="My first car will be "+cars[3].title()+"."
print(msg1)

#Changing, Adding, and Removing Elements

#Modifying Elements in a List
cars[0]='toyota'
print(cars)

#Adding Elements to a List

#Appending Elements to the End of a List
cars.append('audi')
print(cars)
# The append() method makes it easy to build lists dynamically. For example, you can start with an empty list and then add items to the list using a series of append() statements.
bikes=[]
bikes.append('honda')
bikes.append('ducati')
bikes.append('bmw')
print(bikes)

#Inserting Elements into a List
bikes.insert(0,'suzuki') #"0" is the position to be inserted
print(bikes)

#Removing Elements from a List

#Removing an Item Using the del Statement
del bikes[0]
print(bikes)

#Removing an Item Using the pop() Method: for storing the deleted or removed item from the list in a variable. The pop() method removes the last item in a list
popped_bikes1=bikes.pop()
print(bikes)
print(popped_bikes1)

#Popping Items from any Position in a List
popped_bikes2=bikes.pop(0)
print(bikes)
print(popped_bikes1)
print(popped_bikes2)
#note: it will permanently remove bikes from the list "bikes"

#Removing an Item by Value
bikes1=['honda', 'ducati', 'bmw']
bikes1.remove('honda')
print(bikes1)

bikes2=['honda', 'ducati', 'bmw']
too_expensive='bmw'
bikes2.remove(too_expensive)
print(bikes2)
#The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have been removed. You’ll learn how to do this in Chapter 7.

#Organizing a List

#Sorting a List Permanently with the sort() Method: The sort() method, shown at u, changes the order of the list permanently. The items in the list are now in alphabetical order, and we can never revert to the original order.
cycles=['street racer','volcano','keysto','hercules']
cycles.sort()
print(cycles)
#reversing it
cycles.sort(reverse=True)
print(cycles)

#Sorting a List Temporarily with the sorted() Function
print('Here is the original list of cycles:')
print(cycles)

print('\nhere is the sorted list of cycles:')
print(sorted(cycles))

#printing in sorted reverse order
print(sorted(cycles, reverse=True))

#printing in normal reverse order
cycles.reverse()
print(cycles)

#Note: Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several ways to interpret capital letters when you’re deciding on a sort order, and specifying the exact order can be more complex than we want to deal with at this time.

#Finding the Length of a List
print(len(cycles))
#Python counts the items in a list starting with one, so you shouldn’t run into any offby-one errors when determining the length of a list.





alien0={'color':'green','points':5}
print(alien0['color'])
print(alien0['points'])

#Working with Dictionaries
#A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key's value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in dictionary. In Python, a dictionary is wrapped in braces, {Y, with a series of key- value pairs inside the braces, as shown in the earlier example.

#Accessing Values in a Dictionary
newpoints=alien0['points']
print('Yeah!!you just earned '+str(newpoints)+' points!')

#Adding New Key-Value Pairs
alien0['x-position']=0
alien0['y-position']=25
print(alien0)

#Starting with an Empty Dictionary
alien1={}
alien1['color']='red'
alien1['points']=15
alien1['x-position']=45
alien1['y-position']=18
print(alien1)

#Modifying Values in a Dictionary
alien1['color']='blue'
print('Here is the new color: '+alien1['color'].title())

alien2={'color': 'red', 'points': 15, 'x-position': 45, 'y-position': 18, 'speed': 'medium'}
print('Original position of alien2: ('+str(alien2['x-position'])+','+str(alien2['y-position'])+')')

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
alien2['speed']='fast'
if alien2['speed']=='low':
    x_increment=1
    y_increment=0.5
elif alien2['speed']=='medium':
    x_increment=2
    y_increment=1
else:
    x_increment=3
    y_increment=1.5

#The new position:
alien2['x-position']=alien2['x-position']+x_increment
alien2['y-position']=alien2['y-position']+y_increment

print('New position of alien2 is : ('+str(alien2['x-position'])+','+str(alien2['y-position'])+')')

#Removing Key-Value Pairs
print('original alien2 dictionary: '+str(alien2))
del alien2['points']
print(alien2)
#Note: Be aware that the deleted key-value pair is removed permanently. 

#A Dictionary of Similar Objects
favlang={
    'smit':'python',
    'vikram':'html',
    'harsh':'javascript',
    'aarsh':'java'
    }
print("Smit's favourite language is: "+favlang['smit'])

#Looping Through a Dictionary
#A single Python dictionary can contain just a few key-value pairs or millions of pairs. Because a dictionary can contain large amounts of data, Python lets you loop through a dictionary. Dictionaries can be used to store information in a variety of ways; therefore, several different ways exist to loop through them. You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.
#Looping Through All Key-Value Pairs
user0={
    'username':'smit@123',
    'first':'smit',
    'last':'@123'
    }
for key, value in user0.items():
    print("\nkey: "+key)
    print("\nValue: "+value)

favlang={
    'smit':'python',
    'vikram':'html',
    'harsh':'javascript',
    'aarsh':'java'
    }
for name, lang in favlang.items():
    print(name.title()+"'s "+"favourite language is: "+lang.title())

friends=['smit','harsh']
for name in favlang.keys():
    print("\n"+name.title())

    if name in friends:
        print("\tHii "+name.title()+", I see you favourite language is: "+favlang[name].title()+"!")

nonames=['chirag','mihir']
for names in nonames:
    if names not in favlang.keys():
        print("\n"+names.title()+", please take our vote!")
#this was for list

#this will be for dictionary
nonamess={
     'chirag':'xyz',
     'mihir':'abc'
    }
for namess in nonamess.keys():
    if namess not in favlang.keys():
        print("\n\t"+namess.title()+", please take our vote!!")

#Looping Through a Dictionary’s Keys in Order
for name in sorted(favlang.keys()):
    print(name.title()+", thank you for taking the poll!")

#Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for lang in favlang.values():
    print("\t"+lang.title())

#Note:This approach pulls all the values from the dictionary without checking for repeats. That might work fine with a small number of values, but in a poll with a large number of respondents, this would result in a very repetitive list. To see each language chosen without repetition, we can use a set. A set is similar to a list except that each item in the set must be unique.
favbhasha={
    'smit':'python',
    'harsh':'java',
    'aarsh':'python',
    'vikram':'html'
    }
for lang in set(favbhasha.values()):
    print(lang.title())

#Nesting: storing a set of dictionaries in a list or a list of items as a value in a dictionary is called nesting. You can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.






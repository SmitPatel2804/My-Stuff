#Nesting: storing a set of dictionaries in a list or a list of items as a value in a dictionary is called nesting. You can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.

#A List of Dictionaries
alien0={'color': 'green', 'points': 5}
alien1={'color': 'yellow', 'points': 10}
alien2={'color': 'red', 'points': 15}
aliens=[alien0,alien1,alien2]
for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
alienss=[]
# Make 30 green aliens.
for alien_no in range(30):
    new_alien={'color': 'green', 'points': 5, 'speed': 'slow'}
    alienss.append(new_alien)

# Show the first 5 aliens:
for alie_n in alienss[:5]:
    print(alie_n)
print("...")


# Show how many aliens have been created.
print("Total number of aliens: "+str(len(alienss)))

aliensss=[]
for alien_number in range(0,30):
    new_aliens={'color': 'green', 'points': 5, 'speed': 'slow'}
    aliensss.append(new_aliens)
    
for alien in aliensss[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
for alien in aliensss[0:5]:
    print(alien)
print('...')

#A List in a Dictionary
## Store information about a pizza being ordered.
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
    }
## Summarize the order.
print("You ordered a "+pizza['crust']+"-crust pizza"+" with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

favlang={
    'smit':['python','ruby'],
    'vikram':['html','javascript'],
    'harsh':['java','swift']
    }
for name, lang in favlang.items():
    print("\n"+name.title()+"'s favourite languages are:")
    for language in lang:
        print("\t"+language.title())

#A Dictionary in a Dictionary
users={
    'aeinstein':{
        'first':'albert',
        'second':'einstein',
        'location':'vijapur'
    },
    'mcurie':{
        'first':'marie',
        'second':'curie',
        'location':'mehsana'
    }
}
for username, userinfo in users.items():
    print("\nUsername: "+username.title())
    full_name=userinfo['first']+" "+userinfo['second']
    location=userinfo['location']
    
    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())

cars=['audi','bmw','toyota','tata']
for car in cars:
     if car=='bmw':
         print(car.upper())
     else:
         print(car.title())

#Checking Whether a Value Is not in a List
banned_users=['smit','vikram','niru','maitri']
user='smit'
banned_users.remove('smit')
if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")
else:
    print(user.title()+", you are banned for 14 days.")

#if Statements

#Simple if Statements and if-else Statements
age=19
if age>=18:
    print("\nYeah!! you are eligible to vote.")
    print("Have you registered for vote?")
else:
    print("You are too young to vote.")

#The if-elif-else Chain
ummar=19
if ummar<4:
    print('Your admission cost is $0')
elif ummar<=18:
    print('Your admission cost is $5')
else:
    print('your admission cost is $10')

age2=12
if age2<4:
    price=0
elif age2<=18:
    price=5
else:
    price=10
print('Your admission cost is $'+str(price)+'.')

#Using Multiple elif Blocks
#Omitting the else Block

#Testing Multiple Conditions
#using only if condition:
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")
print("\nFinished making your pizza!")
#We start at u with a list containing the requested toppings. The if statement at 50 checks to see whether the person requested mushrooms on their pizza. If so, a message is printed confirming that topping. The test for pepperoni at 52 is another simple if statement, not an elif or else statement, so this test is run regardless of whether the previous test passed or not.

#using if-elif condition:
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")
print("\nFinished making your pizza!")
#The test for 'mushrooms' is the first test to pass, so mushrooms are added to the pizza. However, the values 'extra cheese' and 'pepperoni' are never checked, because Python doesn’t run any tests beyond the first test that passes in an if-elif-else chain.

#Making the use of if-elif-else successful by using for loop which lets python to see every item in the list.
for toppings in requested_toppings:
     if 'mushrooms' in toppings:
         print("\nAdding mushrooms.")
     elif 'pepperoni' in toppings:
         print("Adding pepperoni.")
     elif 'extra cheese' in toppings:
         print("Adding extra cheese.")
print("\nFinished making your pizza!")


#Using if Statements with Lists
#Checking for Special Items
requested_toppings1=['mushrooms','green peppers','origano','extra cheese']
for requested_topping1 in requested_toppings1:
   print("\nAdding "+requested_topping1+" to your pizza!")

requested_toppings2=['mushrooms','green peppers','origano','extra cheese']
for requested_topping2 in requested_toppings2:
 if requested_topping2 == 'mushrooms':
    print("\nSorry, we ran out of green peppers.")
 else:
    print("\nadding ".title()+requested_topping2+' to your pizza!')

#Checking That a List Is Not Empty
requested_toppings3=[]
if requested_toppings3:
   for requested_topping3 in requested_toppings3:
      print("adding ".title()+requested_toppings3+' to your pizza!')
else:
   print('\nAre you sure you want a plain pizza?')

#Using Multiple Lists
available_toppings=['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings4=['mushrooms', 'french fries', 'extra cheese']
for requested_topping4 in requested_toppings4:
   if requested_topping4 in available_toppings:
      print('\nadding '.title()+requested_topping4+' to your pizza.')
   else:
      print("\nSorry, we don't have "+requested_topping4+".")













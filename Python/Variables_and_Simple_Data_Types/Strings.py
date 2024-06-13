name='smit patel'
print(name.title())
print(name.upper())
print(name.lower())

# combining and concatenating strings
firstname='smit'
lastname='patel'
fullname=firstname+' '+lastname
print(fullname)
print('Hello, '+fullname.title()+'!!')

#storing concatenation in a variable and then printing
msg='Hello, '+fullname.title()+'!!'
print(msg)

#Adding Whitespace to Strings with Tabs or Newlines

#To add a tab to your text, use the character combination \t
print('python') #normal
print('\tpython') #tabbed

#To add a newline in a string, use the character combination \n
print('languages:\npython\nC\njava'.title()) #normal
print('languages:\n\tpython\n\tC\n\tjava'.title()) #more structured

#Stripping Whitespace
# Python can look for extra whitespace on the right and left sides of a string. To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
name1='python '
print(name1.rstrip())
name2=' Python'
print(name2.lstrip())
name3=' Python '
print(name3.strip())

# Integers
#You can add (+), subtract (-), multiply (*), and divide (/) integers in Python. 
#Python uses two multiplication symbols to represent exponents
#You can also use parentheses to modify the order of operations so Python can evaluate your expression

#Avoiding Type Errors with the str() Function
age=23
# message="happy "+age+"rd birthday"
#this will show arrow since we have inserted variable in a string...for this we have to make it a string by using str()
message="Happy "+str(age)+"rd Birthday"
print(message)

#The Zen of Python
import this
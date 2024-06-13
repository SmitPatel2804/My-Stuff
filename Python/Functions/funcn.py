#In this chapter you’ll learn to write functions, which are named blocks of code that are designed to do one specific job. When you want to perform a particular task that you’ve defined in a function, you call the name of the function responsible for it. If you need to perform that task multiple times throughout your program, you don’t need to type all the code for the same task again and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function.

#In this chapter you’ll also learn ways to pass information to functions. You’ll learn how to write certain functions whose primary job is to display information and other functions designed to process data and return a value or set of values. Finally, you’ll learn to store functions in separate files called modules to help organize your main program files.

#Defining a function:
def greet_user():
    """Display a simple greeting message"""
#The above statement is called a Docstring which describes the use of the function. It is written inside triple quotes.
    print("Hello!")
greet_user()

#Passing info to the function:
def greetuser(username):
    print("Hello, "+username.title()+"!")
greetuser("smit")
#here the value "username" is called parameter and "smit" is called argument

#Passing Arguments:
#You can use positional arguments, which need to be in the same order the parameters were written; keyword arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values.
#positional arguments: 
#When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called positional arguments.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a "+animal_type)
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')

#multiple function calls:
def describepet(animaltype, petname):
    """Display information about a pet."""
    print("\nI have a "+animaltype)
    print("My "+animaltype+"'s name is "+petname.title()+".")
describepet('dog','shiro')
describepet('cat','cathy')
#Note: Order matters.
#keyword Arguments:
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
#here, the order doesn't matter.

#default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

#Equivalent Function Calls:
def describe_pet(pet_name, animal_type="dog"):
    describe_pet("willie")
    #or 
    decsribe_pet(pet_name="willie")
#Note:avoid argument errors which can be done by writing code like above after defining the function.

#Return Values: A function doesn’t always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function.
#returning a simple value:
def get_formatted_names(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name= first_name+" "+last_name
    return full_name.title()
musician=get_formatted_names("smit","patel")
print("My full name is "+musician)

#making an argument optional
def get_formattedname(surname, firstname, lastname):
    fullname=surname+" "+firstname+" "+lastname
    return fullname.title()
members=get_formattedname("patel","smit","vikrambhai")
print(members)

#putting if-else condition for lastname:
def get_formattedname(surname, firstname, lastname=""):
    if lastname:
        fullname=surname+" "+firstname+" "+lastname
    else:
        fullname=firstname+" "+surname
    return fullname.title()
local=get_formattedname("patel","smit","vikrambhai")
print(local)


    
#printing multiline strings
st = """ekjngkjnkddkjfv dkfv

fd vdkjfvkdf vdfv
dfvkld fd v dlkf vlkdmfvkdffjvndvfvdfvndfv
dfvdkjfvnkjdf vkjd vd
vdkjf vkjd vdj vd
vdvkj dfvkj """
print(st)

name = "Smit"
print(name[0])
print(name[1])
print(name[2])
print(name[3]+"\n")
#print(name[4]) throws error

print("Lets use for loop: ")
#looping through strings
for char in name:
    print(char)



#string slicing
names="Smit,Harry"
print(names[0:])
print(names[0:11])
print(len(names))

#slicing is not used by parenthasis
fruit="mango"
mangolen=len(fruit)
print(mangolen)
print(fruit[0:4])
print(fruit[0:])
print(fruit[:4])
print(fruit[1:4])
print(fruit[:])
print(fruit[0:-3]) #here it is default print(fruit[0:len(fruit)-3])
print(fruit[-1:-3]) #it will be -3:-1 and then len(fruit)-3 : len(fruit)-1
print(fruit[-3:-1])

#String Methods
#Note: Strings are immutable
a="!!!!!!!!sMiT!!!!!!!"
print(a.upper())
c=a.strip("!")
b=c.lower()
print(a.capitalize())
print(a.rstrip("!"))
print(a.lstrip("!"))
print(b.replace("smit","Harry"))
print(a.split(" "))
str1="welcome to the console!!!"
str2=str1.center(50)
print(len(str1))
print(str2)
print(len(str2))
print(a.count("Smit"))
print(str1.endswith("!!!")) #boolean return
print(str1.endswith("to",4,10)) #boolean return
str3="My name is smit."
print(str3.find("is")) #return the index of the first occurence

#difference between find() and index()
print(str3.find("ishh")) #will return -1
# print(str3.index("ishh")) #will return error

str4="Welcome To the Console"
print(str4.isalnum()) #return true if the entire string consist of A-Z, a-z or 0-9 and return false if any other characters or any punctuation is used.
str5="WelcomeToTheConsole"
print(str5.isalnum())

print(str5.isalpha()) #for only alphabets
print(str4.isalpha()) #for only alphabets
print(str4.isprintable())
print(str5.islower())
print(str5.isupper())
str6="        "
print(str6.isspace())
print(str4.istitle())
print(str4.startswith("Welcome"))
print(str4.swapcase())
print(str4.title())


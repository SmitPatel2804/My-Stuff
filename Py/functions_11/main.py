# def calculategmean():
#     a = float(input("A: "))
#     b = float(input("B: "))
#     mean=(a*b)/(a+b)
#     print(mean)
#calculategmean()

def greaternum():
    a = int(input("A: "))
    b = int(input("B: "))
    if a > b:
        print("A is greater than B.")
    elif a < b:
        print("B is greater than A.")
    else:
        print("A and B are equal.")

#greaternum()

#if you want to define a function and code it after some time...then you can use pass.
def xyz():
    pass

#we can provide default value to the function and then we can modify it.
#example
def avg(a=9, b=1):
    print("Average is:",(a+b)/2)

avg(1, 2)

#IMP
#arbitrary numbers of arguments
def fullname(*name):
    print(type(name))
    print("Hello", name[0].title(),name[1].title(),name[2].title())

fullname("smit","vikrambhai","patel")

#Benefit: no need to make many numbers of variables for storing values.

#NOTE: for tuple: you can use "*" while defining function.
# for dictionary: you can use "**" while defining function, but we need to declare it with key-value pairs.
#example
def terenaam(**naam):
    print("Hello", naam["fname"].title(), naam["mname"].title(), naam["lname"].title())
#order doesn't matter here
terenaam(fname="smit",lname="patel",mname="vikrambhai")
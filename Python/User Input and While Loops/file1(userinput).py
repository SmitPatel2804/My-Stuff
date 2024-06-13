#name=input("Type your name here: ")
#print("Hello "+name.title())
#You can store your prompt in a variable and pass that variable to the input()function. This allows you to build your prompt over several lines, then write a clean input() statement.
#prompt="If you tell us who you are, we can personalize the messages you see."
#prompt+="\nWhat is your first name?"
#name=input(prompt)
#print("\nHello, "+name.title()+"!")
#This example shows one way to build a multi-line string. The first line stores the first part of the message in the variable prompt. In the second line, the operator += takes the string that was stored in prompt and adds the new string onto the end.

#Using int() to Accept Numerical Input
#age=input("How old are you? ")
#print("Your age is: " + age)
#In order to run conditional tests, the numerical variable should be converted from string to integer by using int() funcn.
# age=input("Enter your age: ")
# age=int(age)
# if age>=18:
#     print("\nYeah, you are eligible to vote!!")
# else:
#     print("\nYou are too young to vote.")

#The Modulo Operator
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))
if denominator!=0:
    remainder=numerator%denominator
    print("Remainder of "+str(numerator)+" divided by "+str(denominator)+" is: "+str(remainder))
else:
    print("Denominator should not be equal to zero")




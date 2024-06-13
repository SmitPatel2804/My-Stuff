#Introducing while Loops
# current_number=1
# while current_number<=5:
#     print(current_number)
#     current_number+=1
#In the first line, we start counting from 1 by setting the value of current_number to 1. The while loop is then set to keep running as long as the value of current_number is less than or equal to 5. The code inside the loop prints the value of current_number and then adds 1 to that value with current_number += 1.
#Python repeats the loop as long as the condition current_number <= 5 is true. Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2. Because 2 is less than 5, Python prints 2 and adds 1 again, making the current number 3, and so on. Once the value of current_number is greater than 5, the loop stops running and the program ends

#Letting the User Choose When to Quit
# prompt="\nTell me something, and I will repeat it back to you."
# prompt+="\nEnter 'quit' to end the program."
# message=""
# while message!="quit":
#     message=input(prompt)
    
#     if message!='quit':
#         print(message)
#At "prompt", we define a prompt that tells the user their two options: entering a message or entering the quit value (in this case, 'quit'). Then we set up a variable "message" to store whatever value the user enters. We define message as an empty string, "", so Python has something to check the first time it reaches the while line. The first time the program runs and Python reaches the while statement, it needs to compare the value of message to 'quit', but no user input has been entered yet. If Python has nothing to compare, it won’t be able to continue running the program. To solve this problem, we make sure to give message an initial value. Although it’s just an empty string, it will make sense to Python and allow it to perform the comparison that makes the while loop work. This while loop runs as long as the value of message is not 'quit'. The first time through the loop, message is just an empty string, so Python enters the loop. At message = input(prompt), Python displays the prompt and waits for the user to enter their input. Whatever they enter is stored in message and printed; then, Python reevaluates the condition in the while statement. As long as the user has not entered the word 'quit', the prompt is displayed again and Python waits for more input. When the user finally enters 'quit', Python stops executing the while loop and the program ends:

#This program works well, except that it prints the word 'quit' as if it were an actual message.
#for avoiding printing "Quit" when quit is written, we use if statement.

#what if "QUIT or QuIt or any other combination is used" instead of "quit"?
# promppt = "\nTell me something, and I will repeat it back to you "
# promppt += "or enter 'quit' to end the program: "

# messsage = ""
# while messsage.lower() != "quit":
#     messsage = input(promppt)
    
#     if messsage.lower() != "quit":
#         print(messsage)

#Using a flag
#For example, in a game, several different events can end the game. When the player runs out of ships, their time runs out, or the cities they were supposed to protect are all destroyed, the game should end. It needs to end if any one of these events happens. If many possible events might occur to stop the program, trying to test all these conditions in one while statement becomes complicated and difficult. For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. As a result, our overall while statement needs to check only one condition: whether or not the flag is currently True.

# text="\nHey there! tell me something and i will repeat it back to you "
# text+="\nor enter 'quit' to end the program: "
# active=True
# while active:
#     msg=input(text)
#     if msg.lower()=='quit':
#         active=False
#     else:
#         print(msg)

#Using break to Exit a Loop
#To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement. 
# mesg="\nPlease enter the name of city you have visited "
# mesg+="\n (Enter 'quit' when you are finished.): "
# while True:
#     city=input(mesg)
#     if city.lower()=='quit':
#         break
#     else:
#         print("I'd love to go to "+city.title()+"!")
#A loop that starts with while True u will run forever unless it reaches a break statement. The loop in this program continues asking the user to enter the names of cities they’ve been to until they enter 'quit'. When they enter 'quit' , the break statement runs, causing Python to exit the loop.

#Using continue in a Loop
currentnumber=0
while currentnumber<10:
    currentnumber+=1
    if currentnumber%2==0:
        continue
    print(currentnumber)
#first, we gave command that currentnumber is 0 and set a limit of currentnumber <10, then we set that if remainder of currentnumber/2 is 0 then add 1 to that number and print it.

#Avoiding Infinite Loops
#example of a while loop counting from 1 to 5
cn=1
while cn<=5:
    cn+=1
    print("\n"+str(cn))
#Note: the output will show numbers starting from 2 to 6 since we have passed cn+=1 before print function so it will add 1 first and then print it. 
#correction
c_n=1
while c_n<=5:
    print("\n"+str(c_n))
    c_n+=1

#example of infinite loop
# x=1
# while x<=5:
#     print(x)

#Using a while Loop with Lists and Dictionaries
#through the while loop, we’d receive another input value and respond to that. But to keep track of many users and pieces of information, we’ll need to use lists and dictionaries with our while loops. A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list. To modify a list as you work through it, use a while loop. Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later. 

#Moving Items from One List to Another
#star with users that need to be verified and an empty list to hold the confirmed users.
unconfirmed_users=['smit','vikram','maitri','niru']
confirmed_users=[]
#Verify each user until there are no more unconfirmed users and Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
#Note:popping users from unconfirmed list will be done from the end since pop removes items from end, but if you want to pop the items from the beginning, put 0 in pop().
    print("verifying User: "+current_user.title())
    confirmed_users.append(current_user)
#Display all confirmed users:
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Removing All Instances of Specific Values from a List
pets=['dog','cat','pig','cat','goldfish','cat','rabbit']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#Filling a Dictionary with User Input
responses={}
#set the flag to indicate that polling is active
polling_active=True
while polling_active:
    #prompt for person's name and response.
    name=input("\nWhat is your name? ").title()
    response=input("Which mountain would you like to climb? ").title()

    #store the response in the dictionary:
    responses[name]=response
    print(responses)

    #find out if anyone else is going to take the poll.
    repeat=input("\nWould you like to let another person respond? (yes/no) ")
    if repeat.title()=="No":
        polling_active=False

#polling is complete. show the results.
print("\n-----Poll Results-----")
for name, response in responses.items():
    print(name+" would like to climb "+response+".") 

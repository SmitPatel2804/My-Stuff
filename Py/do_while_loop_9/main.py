# while True:
#     number = int(input("Enter a number: "))
#     print(number)
#     if(number>=0):
#         print("You have entered a positive number.")
#         break
#     else:
#         print("You have entered a negative number.")
#         break

while True:
    number = int(input("Enter a number: "))
    if not number>0:
        break
    else:
        print("Number is positive.")
a=int(input("Enter a number: "))
match a:
    #if a = 0
    case 0:
        print("Number is zero.")
    case _:
        if(a<=10 and a>=0):
            print("Number is between 0 to 10.")
        # we use "_" for default in python
        #Note: we use break statement in c/c++ but not used in python.


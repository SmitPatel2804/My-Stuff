for i in range(11):
    print("5 x",i+1, "=",5*(i+1))
    if(i==10):
        break
# This will have no effect on loop
 #for effect to act
for i in range(11):
    if (i == 10):
        break
    print("5 x", i + 1, "=", 5 * (i + 1))

# NOTE : Break means "loop ko chhod kar nikal jao."
# Continue means "Iteration ko chhod kar nikal jao."
#continue mai jo condition di hai...usko skip kar dega aur next par chala jayega
#example:
for i in range(12):
    if (i == 10):
        print("Skip the iteration.")
        continue
    print("5 x", i + 1, "=", 5 * (i + 1))

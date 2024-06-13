letter=str(input())
distinct_char=set(letter)
num=len(distinct_char)
if(num<=100):
    if(num%2==0):
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
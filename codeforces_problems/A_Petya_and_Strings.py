str1=str(input())
str2=str(input())
li1=[]
n=len(li1)-1
li2=[]
letter={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
list1=[]
list2=[]
for i in str1:
    char1=i.lower()
    li1.append(char1)
for l in str2:
    char2=l.lower()
    li2.append(char2)

for i in li1:
    for alp in letter.keys():
        if(i==alp):
            list1.append(letter[i])

for l in li2:
    for shabd in letter.keys():
        if(l==shabd):
            list2.append(letter[l])

string_combined1=''.join(map(str, list1))
string_combined2=''.join(map(str, list2))

integer_1=int(string_combined1)
integer_2=int(string_combined2)

if(integer_1>integer_2):
    print("1")
elif(integer_1<integer_2):
    print("-1")
else:
    print("0")


#conversion of one data type to other data type is typecasting.
#eg: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict() etc...
# 1. explicit typecasting
# 2. implicit typecasting

#explicit typecasting

# a = 1
# b = 2
# print(a+b)
# answer: 3

'''
a = "1"
b = "2"
print(a+b)
answer: 12
'''

'''
a = "1"
b = "2"
print(int(a)+int(b))
answer: 3
'''

#implicit typecasting
c = 9
d = 1.5
print(c+d)
print(type(c+d))
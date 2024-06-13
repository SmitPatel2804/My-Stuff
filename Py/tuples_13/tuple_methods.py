# in order to make a list into tuple, you need to convert it into list and then back into tuple
countries = ("India","Spain","Italy","England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
countries=tuple(temp)
print(countries)

#tuples can be concatenated directly
countries2=("Afghanistan","Bangladesh","China","Saudi")
countries3=countries+countries2
print(countries3)

print(countries3.count("India"))
print(countries3.index("India"))

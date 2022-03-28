# Python List index example
# create list object and assign it to variable l
l = ['a','b','c','d','e','b','c']

# calling index() method by passing 'b' as an argument
index = l.index('e')

# print the value of variable index
print(index)

# calling index() method by passing 'b' and starting index 2
index = l.index('e',2)

# print the value of variable index
print(index)

# calling index() method by passing 'b', 0 as starting index and 2 as ending index
index = l.index('e',0,2)

# print the value of variable index
print(index)
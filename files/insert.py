from itertools import count


list=[100,"Hello",120,"rahul"]
print('list: ', list)
# insert at the place where the datatype of existing and inserting element is same.
list.insert(2,"world") 
print('list: ', list)
print("elements in the list: ", list.count(100))
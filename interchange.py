"""
Interchange first and last element of list.
"""
List = []
n = int(input("Enter the total no of elements of the list"))
for i in range(0,n):
    List.append(input("Enter the element"))
for i in List:
    print(i, end=",")
x = List[0]
List[0] = List[n-1]
List[n-1] = x
print(List) 

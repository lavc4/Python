# remove the element from the list
l1 = []
n = int(input("Enter total no of elemets"))
for i in range(0,n):
    l1.append(input("Enter the element"))
print(l1)
l1.remove(input("Enter the element which u wanna remove"))
print("Updated list: %s"%(l1))
list = [1, 2, 3, 4, 5]
d = int(input("Enter the number"))
for i in range(0, len(list)):
    if list[i] == d:
        break
    i += 1
list.insert(0, list.pop(i))
print(list)

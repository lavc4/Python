list = [1, 2, 3, 4, 5]
d = int(input("Enter the number"))
for i in range(0, len(list)):
    if list[0] != d:
        if list[i] == d:
            print (i)
        i +=1
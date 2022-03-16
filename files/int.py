n = int(input("Enter the number: "))
i = 1
s = 0
x = "1"
while  i<=n:
    s = s+i
    # if i == 1:
    #     x = x
    # else:
    #     x = x + "+" + str(i)
    # print(x + "=" + str(s))
    # i+=1
    
    # Alternative
    print(x, "=", s)
    i += 1
    x = x + "+" + str(i)
    
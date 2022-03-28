list = [11, 22, 33, 44, 55, 66, 77, 88, 99]
s1 = ["He", "is", "a", "Boy"]
list[-3:-1] = ["rahul", 88.09]
print(type(s1))
print(type(list))
# del list[-3]
# print(list)
# print(str)
# for i in list:
#     print(str)
"""
List operations
"""
# Concatenation it joints two strings end by end 
print(list+s1)
# Repetition it multiplies the string
print(list*2)
# Membership, it uses to find the element in the list
print("rahul" in list)
print(f"the value of s1[0][1] :{s1[0][1]}")
s2 = [["hello world", 87], 45, "string"]
print(f"the value of s2[0][0][3] :{s2[0][0][3]}")

list.append()
print(list)
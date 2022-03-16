import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names = ["Lav", "Priyanshi", "Hammadoon Sir", "Shivam Sir", "Aaryan", "Harshita", "Anil", "Ankit"]
print(f"{names[random.randint(0, len(names)-1)]} is going to buy the meal today!")
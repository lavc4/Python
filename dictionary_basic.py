# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Dictionary before changing the year:\n{thisdict}")
thisdict["year"] = 2018
print(f"Dictionary after changing the year:\n{thisdict}")

x = thisdict.values()
print(x)

y = thisdict.keys()
print(y)

# clear the dictionary
thisdict = {}
print(thisdict)
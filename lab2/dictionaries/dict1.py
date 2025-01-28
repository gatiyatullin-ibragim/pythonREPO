#Dictionaty is like map in c++
#it contains the key-value pairs

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#DICTIONARY ITEMS ARE ORDERED, CHANGEABLE, AND DO NOT ALLOW DUPLICATES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#output: Ford


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


#Print the number of items in the dictionary:
print(len(thisdict))



#The values in dictionary items can be of any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}



#Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


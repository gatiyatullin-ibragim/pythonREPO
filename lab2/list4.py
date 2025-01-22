#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""
Insert Items.
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert an item as the second position:
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#extending list:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']



"""Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:
"""
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']



#You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)



"""
Another way to make a copy is to use the built-in method list().

Example
Make a copy of a list with the list() method:
"""
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

"""
You can also make a copy of a list by using the : (slice) operator.

Example
Make a copy of a list with the : operator:
"""
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
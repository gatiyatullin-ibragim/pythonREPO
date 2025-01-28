#example of sets:
myset = {"apple", "banana", "cherry"}

"""
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
"""

#the set is in brackets: {}

#Set items are unordered, unchangeable, and do not allow duplicate values.

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)



#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)



#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


#we also can get the length of the set using the function len()
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}


#What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))


#or we may use a set constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

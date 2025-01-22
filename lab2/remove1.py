# The remove() method removes the specified item.

# ExampleGet your own Python Server
# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# If there are more than one item with the specified value, the remove() method removes the first occurrence:

# Example:
# Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.

# # Example:
# # Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)



#Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


#Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.

# Example:
# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist


"""The clear() method empties the list.

The list still remains, but it has no content.
"""
# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

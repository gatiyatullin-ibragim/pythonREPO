#Customize Sort Function

#sorting using function:
#Sort the list based on how close the number is to 50:
def foo(n):
    return abs(n-50)

thislist = [100,50,65,82,23]
thislist.sort(key = foo)
print(thislist)



# Example:
# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#output:['banana', 'cherry', 'Kiwi', 'Orange']

#and .reverse reverse the order of the list
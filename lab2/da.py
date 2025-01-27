#unpack tuples

#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#Packing a tuple:
fruits = ("apple", "banana", "cherry")


#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
"""
Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
"""

#ASTERISK:
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
#Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#output: 
# apple
# banana
# ['cherry', 'strawberry', 'raspberry']



#Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#output:
# apple
# ['mango', 'papaya', 'pineapple']
# cherry
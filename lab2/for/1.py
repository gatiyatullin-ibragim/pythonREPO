"""
Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

Example
Print each fruit in a fruit list:
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  


#Loop through the letters in the word "banana":
for x in "banana":
  print(x)
  

#Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  

#Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
"""
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Example:
Using the range() function:
"""
for x in range(6):
  print(x)


#Using the start parameter:
for x in range(2, 6):
  print(x)
  
  
#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)


#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#Example:
#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
  
  
#Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")  
"""
output:
0
1
2
"""


"""A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop":
Example:
Print each adjective for every fruit:
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
#Example:
for x in [0, 1, 2]:
  pass


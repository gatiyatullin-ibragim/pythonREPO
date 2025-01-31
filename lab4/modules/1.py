# To create a module just save the code you want in a file with the file extension .py:
# Example
# Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)
  
  
  
# Now we can use the module we just created, by using the import statement:

# Example
# Import the module named mymodule, and call the greeting function:
import mymodule

mymodule.greeting("Jonathan")




#Import the module named mymodule, and access the person1 dictionary:
import mymodule

a = mymodule.person1["age"]
print(a)



#Create an alias for mymodule called mx:
import mymodule as mx

a = mx.person1["age"]
print(a)



#Import and use the platform module:
import platform

x = platform.system()
print(x)


#List all the defined names belonging to the platform module:
import platform

x = dir(platform)
print(x)


#The module named mymodule has one function and one dictionary:
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}



#Import only the person1 dictionary from the module:
from mymodule import person1

print (person1["age"])


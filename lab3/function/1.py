#In Python a function is defined using the def keyword:
#Example:
def my_function():
  print("Hello from a function")


# To call a function, use the function name followed by parenthesis:

# Example:
def my_function():
  print("Hello from a function")

my_function()


"""
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

Example:
"""
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

"""
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

Example:
This function expects 2 arguments, and gets 2 arguments:
"""
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
#Example:
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
#Example:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



#To let a function return a value, use the return statement:
#Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass



"""
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:
"""
def my_function(x, /):
  print(x)

my_function(3)



#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)

my_function(x = 3)


#ERROR example:
def my_function(x, /):
  print(x)

my_function(x = 3)


#To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)


#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)

my_function(3)


#ERROR example:
def my_function(*, x):
  print(x)

my_function(3)


"""
Combine Positional-Only and Keyword-Only
You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
"""
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
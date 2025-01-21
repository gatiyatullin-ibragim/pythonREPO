#formating

age = 36
txt = "My name is John, I am " + age
print(txt)
#output will be error



#to output string with integer we use f-string or format() method

age = 36
txt = f"My name is John, I am {age}"
print(txt)
#this will be correct

#or

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#Display the price with 2 decimals:


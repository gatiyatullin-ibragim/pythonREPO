print(bool("Hello"))
print(bool(15))

'''
output:
true
true
'''


print(bool(0))

#output: 0

""" 
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""
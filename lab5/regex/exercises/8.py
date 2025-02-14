import re

def split_at_uppercase(string):
    pattern = r'(?=[A-Z])'
    split_string = re.split(pattern, string)
    return split_string

split_str = str(input())
print(split_at_uppercase(split_str))
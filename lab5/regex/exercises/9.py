import re

def insert_spaces(str):
    pattern = r'(?<!^)(?=[A-Z])'
    spaces_string = re.sub(pattern, ' ', str)
    return spaces_string

string = str(input())
print(insert_spaces(string))
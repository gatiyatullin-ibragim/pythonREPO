import re

def replace_characters(input_string):
    pattern = r'[ ,.]'
    result = re.sub(pattern, ':', input_string)
    return result

input_string = "Hello, world. How are you today?"
replaced_string = replace_characters(input_string)
print("Original string:", input_string)
print("Modified string:", replaced_string)

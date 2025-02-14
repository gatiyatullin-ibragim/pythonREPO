import re

def match_string(input_string):
    pattern = r'a.*b$'
    match = re.search(pattern, input_string)
    return bool(match)

input_string = "a_random_sequence_b"
if match_string(input_string):
    print(f"'{input_string}' matches the pattern.")
else:
    print(f"'{input_string}' does not match the pattern.")

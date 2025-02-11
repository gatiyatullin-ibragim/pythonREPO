import re

def match_string(s):
    pattern = r"^a*b*$"
    if re.fullmatch(pattern, s):
        return "Match found!"
    else:
        return "No match."

print(match_string("a"))      
print(match_string("ab"))      
print(match_string("abb"))     
print(match_string("b"))       
print(match_string("ba"))

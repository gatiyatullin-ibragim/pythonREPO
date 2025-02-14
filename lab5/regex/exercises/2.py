import re

def match_strings(s):
    pattern = r"ab{2,3}"
    if re.fullmatch(pattern,s):
        return "Match found"
    else:
        return "no match"
    

string = str(input())
match_strings(string)
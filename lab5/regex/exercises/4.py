import re
def find_sequences(str):
    pattern = r'\b[A-Z]+[a-z]+\b'
    matches = re.findall(pattern, str)
    return matches


string = str(input())
sequences = find_sequences(string)
print(sequences)
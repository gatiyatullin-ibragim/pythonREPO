import re
def find_sequences(str):
    pattern = r'\b[a-z]+_[a-z]+\b'
    matches = re.findall(pattern, str)
    return matches


string = str(input())
sequences = find_sequences(string)
print(sequences)
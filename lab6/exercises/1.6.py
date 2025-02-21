import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt" 
    with open(filename, "w") as f:
        f.write(f"This is {filename}\n")

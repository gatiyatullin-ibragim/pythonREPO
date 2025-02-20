def counter(stroka):
    cntlower=0
    cntupper=0
    for letter in stroka:
        if letter.isupper():
            cntupper += 1
        if letter.islower():
            cntlower += 1
    
    return cntlower, cntupper
            
            
text = str(input())
print(counter(text))

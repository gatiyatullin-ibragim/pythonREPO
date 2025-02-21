def ispolindrom(str):
    if str[::-1] == str:
        return True
    else:
        return False
    
    
string = str(input("enter the string: "))
print(ispolindrom(string))
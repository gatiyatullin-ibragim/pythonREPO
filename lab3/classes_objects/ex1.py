#zadachi
class StringHandler:
    def __init__(self):
        self.string = ""
    
    def getstring(self):
        self.string = input("enter string: ")
        
    def printstring(self):
        print(self.string.upper())
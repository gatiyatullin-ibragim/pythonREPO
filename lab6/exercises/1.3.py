import os

def exist_or_not(path):
    return os.path.exists(path)
    

def filename_and_directoryPortion(path):
    directory = os.path.dirname(path)
    filename = os.path.basename(path)
    
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
 
    
#example
pth = input("enter path: ")
if exist_or_not(pth):
    filename_and_directoryPortion(pth)
else:
    print("Path does not exist")
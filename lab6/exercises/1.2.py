import os

def checking(path):
    print(f"checking acces for {path}")
    print("-" * 40)
    
    if os.path.exist(path):
        print("Path exists!")
    else:
        print("Path does not exist")
        return
    
    
    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not readable")
       
         
    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not writable")
        
    
    if os.access(path, os.X_OK):
        print("Exucutable")
    else:
        print("Not, executable")
    

path = "some_path"
checking(path)
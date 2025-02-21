import os


def list_contents(path):
    all_items = os.listdir(path)
    
    
    directories = [item for item in all_items if os.path.isdir(os.path.join(path,item))]
    
    
    files = [item for item in all_items if os.path.isfile(os.path.join(path,item))]
    
    print(f"Directories in '{path}':", directories)
    print(f"Files in '{path}':", files)
    print(f"All contents in '{path}':", all_items)
    
    
    
path = "."
list_contents(path)
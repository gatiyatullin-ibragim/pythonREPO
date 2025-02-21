import os

def delete_file(path):
    if os.path.exists(path): 
        if os.access(path, os.W_OK): 
            os.remove(path)
            print(f"'{path}' deleted successfully.")
        else:
            print(f"No permission to delete '{path}'.")
    else:
        print(f"File '{path}' does not exist.")

# Пример использования
file_path = "test.txt"
delete_file(file_path)

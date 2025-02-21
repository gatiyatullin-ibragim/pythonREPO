def list_to_file(lst):
    f = open("lst.txt", "w")
    f.writelines(line + "\n" for line in lst)



data = ["Hello", "World", "Python"]
list_to_file(data)
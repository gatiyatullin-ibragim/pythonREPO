def copyfile(source, destination):
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read()) 

copyfile("source.txt", "destination.txt")

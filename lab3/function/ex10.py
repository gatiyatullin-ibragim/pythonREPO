def unique_list(list):
    uniquelist = []
    for x in list:
        if x not in uniquelist:
            uniquelist.append(x)
    return uniquelist


array = []
for i in range(5):
    a = int(input())
    array.append(a)
    
print(unique_list(array))
#joining sets
"""There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
    """
    
#Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


#Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#output:{'b', Elena, 'a', 2, 3, 'c', banana, cherry, 1, John, apple}


#Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)


#Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)



#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#output:{2, 'b', 1, 'c', 3, 'a'}


"""Intersection
Keep ONLY the duplicates

The intersection() method will return a new set, that only contains the items that are present in both sets.
"""
#Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
#output: {'apple'}

#You can use the & operator instead of the intersection() method, and you will get the same result.
#Example
#Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)


#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
#Example
#Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)


set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}
set3 = set1.intersection(set2)
print(set3)
#output:{False, True, 'apple'}



#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
#Example
#Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)


#You can use the - operator instead of the difference() method, and you will get the same result.
#Example
#Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
#output: {'banana', 'cherry'}


#Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
#output:{'banana', 'cherry'}



# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# Example
# Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
#output:{'banana', 'cherry'}

"""You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result."""



#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)



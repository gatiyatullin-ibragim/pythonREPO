def all_true(tup):
    return all(tup)

print(all_true((True, 1, "Hello")))  
print(all_true((True, 0, "Hi")))
print(all_true((False, True)))
def area_of_parallelogram(len_of_base, high_of_parrallelogram):
    return len_of_base * high_of_parrallelogram
    
    
    
lenofbase = float(input("lenght of base: "))
high = float(input("enter the height: "))


print(f"the area of parrallelogram is {area_of_parallelogram(lenofbase, high)}")
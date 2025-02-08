def area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height



base1 = float(input("first base: "))
base2 = float(input("second base: "))
height = float(input("height: "))

print(area_of_trapezoid(base1, base2,height))
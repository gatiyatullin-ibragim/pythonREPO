import math

def area_of_polygon(n,s):
    area = (n*s**2)/(4*math.tan(math.pi/n))
    return area


n = int(input("enter number of sides: "))
s = float(input("enter the lenght of a side: "))


area = area_of_polygon(n,s)


print(f"The area of the regular polyogn is: {area}")
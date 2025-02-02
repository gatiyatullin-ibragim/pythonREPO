def volumeOfTheSphere(radious):
    pi = 3.14
    volume = (4/3)*pi*radious**3
    print(f"the volume of the sphere: {volume}")

rad = int(input("enter radious: "))
print(volumeOfTheSphere(rad))
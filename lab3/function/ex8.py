def spy_game(nums):
    list007 = [0,0,7]
    list1 = []
    for i in nums:
        if i == 0 or i == 7:
            list1.append(i)
    
    if list007 == list1:
        return True
    return False


a = int(input())
chisla = []
for i in range(a):
    b = int(input())
    chisla.append(b)

print(spy_game(chisla))




"""
4
7
0
0
5
False
"""

"""
4
0
0
7
5
True
"""
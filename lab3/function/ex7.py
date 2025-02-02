def has_3_near_to_3(nums):
    for x in range(len(nums)):
        if nums[x]==3 and nums[x+1]==3:
            return True
    return False
        
list = []
for i in range(3):
    a = int(input())
    list.append(a)


print(has_3_near_to_3(list))
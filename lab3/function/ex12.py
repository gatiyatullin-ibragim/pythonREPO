def histogram(list):
    for i in list:
        print('*' * i)


a = int(input("количество колонн: "))
lst = []
for x in range(a):
    a = int(input())
    lst.append(a)
    
histogram(lst)

"""
количество колонн: 4
2
3
3
4
**
***
***
****
"""
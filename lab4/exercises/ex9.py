def from_n_to_0(num):
    for i in range(num, -1, -1):
        yield i
        
n=int(input())
for number in from_n_to_0(n):
    print(number)
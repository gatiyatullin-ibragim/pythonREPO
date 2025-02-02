def isprime(num):
    if num < 2:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True


def filter_prime(list):
    primes = [i for i in list if isprime(i)]
    print(primes)
    
    
array = []
for i in range(6):
    a=int(input())
    array.append(a)

filter_prime(array)
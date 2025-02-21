import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

num = int(input("enter a number: "))
delay = int(input("enter a delay: "))

print(f"Calculating square root of {num} after {delay}ms...")
result = delayed_sqrt(num, delay)
print(f"Result: {result}")

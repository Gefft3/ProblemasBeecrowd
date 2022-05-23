import math

def fat(n):
    if n < 0:
        return 0
    x = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) /2.0))
    return math.floor(x) + 1
    
n = int(input())
print(fat(n))
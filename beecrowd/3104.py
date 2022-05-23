def mod(num, a):

    res = 0
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a
        
    return res
    
b = input()
a = int(input())
print(mod(b, a))
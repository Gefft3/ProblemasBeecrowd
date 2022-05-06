n = int(input())
count = 1
a = 0
b = 0
c = 1
while(count<=n):
    if count == n:
        print(b)
    else: 
        print(b, end=" ")
    a = b
    b = c
    c = a+b
    count+=1

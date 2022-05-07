x = int(input())
y = int(input())
s=0
if x > y:
    for i in range(y+1,x):
        if i%2==1:
            s+=i
else:
    for i in range(x,y):
        if i%2==1:
            s+=i
print(s)

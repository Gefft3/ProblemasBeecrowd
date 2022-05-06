a = int(input())
b = int(input())
if a>=b:
    y = a
    x = b
else:
    y = b
    x = a

for i in range(x+1, y):
    if i%5==2 or i%5==3:
        print(i)
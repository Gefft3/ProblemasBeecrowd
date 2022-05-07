n = int(input())
c = 0
s = 0
lista = ""
while True:
    if c == n: break
    x, y = map(int, input().split())
    if x > y:
        for i in range(y+1,x):
            if i%2==1:
                s+=i
    elif x < y:
        for i in range(x+1,y):
            if i%2==1:
                s+=i
    elif x == y:
        s=0
    lista += str(s)+'\n'
    c+=1
    s=0
print(lista.rstrip())
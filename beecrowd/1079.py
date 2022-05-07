n = int(input())
c = 0
media = 0
lista = ""
while c<n:
    x,y,w = map(float, input().split())
    media = round(((x*2)+(y*3)+(w*5))/10,1)
    lista += str(media)+"\n"
    c+=1

print(f"{lista.rstrip()}")
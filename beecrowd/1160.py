n = int(input())
cont = 0
a = 0
lista = ""
an = ""
while True:
     if cont==n: break
     pa, pb, txa, txb = map(float, input().split())
     while(pa<=pb):
         pa += int(pa*(txa/100))
         pb += int(pb*(txb/100))
         a+=1
         if a>100:
             an = "Mais de 1 seculo.\n"
             break
         else:
             an = str(a)+" anos.\n"
     lista += an    
     cont+=1
     a = 0
print(lista.rstrip())
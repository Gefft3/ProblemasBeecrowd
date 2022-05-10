a1 = int(input()) 
a2 = int(input())
a3 = int(input())

tp1 = (a2*2)+(a3*4)
tp2 = (a1*2)+(a3*2)
tp3 = (a1*4)+(a2*2)

ad = [tp1, tp2,tp3]
tp = 99999999

for i in ad:
    if i<tp:
        tp = i

print(tp)
n = float(input())
n -= 2000
v = 0
r = 0

if n<=0:
    print("Isento")
elif n>0 and n<=1000:
    v = n*0.08
    print(f"R$ {v:.2f}")
elif n>1000 and n<=2500:
    r = n-1000
    v += r*0.18+(1000*0.08)
    print(f"R$ {v:.2f}")
elif n>2500:
    r = n-2500
    v = (r*0.28)+(1000*0.08)+(1500*0.18)
    print(f"R$ {v:.2f}")
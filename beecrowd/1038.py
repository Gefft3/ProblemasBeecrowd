a, b = map(int, input().split())
t = 0 
if a == 1:
    t = 4*b
elif a == 2:
    t = 4.5*b
elif a == 3:
    t = 5*b
elif a == 4:
    t = 2*b
elif a == 5:
    t = 1.5*b
print(f"Total: R$ {t:.2f}")

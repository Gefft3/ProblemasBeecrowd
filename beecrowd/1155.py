s = 0
c1 = 1
c2 = 0
while c1<41:
    s += (c1/(2**c2))
    c1+=2
    c2+=1
    
print(f"{s:.2f}")
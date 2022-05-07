a, b, c = map(int, input().split())
p, s, t = 0,0,0


if a > b and a > c:
    p = a
    if b > c:
        s = b 
        t = c
    else: 
        s = c
        t = b 
if b > a and b > c:
    p = b 
    if a > c:
        s = a
        t = c
    else: 
        s = c 
        t = a
if c > a and c > b:
    p = c
    if a > b:
        s = a 
        t = b
    else: 
        s = b 
        t = a

print(f"{t}\n{s}\n{p}")
print(f"\n{a}\n{b}\n{c}")

a, b, c = map(float, input().split())

if (a>abs(b-c) and a<b+c) or (b>abs(a-c) and b<a+c) or (c>abs(a-b) and c<(a+b)):
    soma = a+b+c
    print(f"Perimetro = {soma:.1f}")
else: 
    area = ((a+b)*c)/2
    print(f"Area = {area:.1f}")

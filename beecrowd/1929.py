a,b,c,d = map(int, input().split())
if (abs(a-b) < c < a+b) and (abs(c-b) < a < c+b) and (abs(a-c) < b < a+c):
    print("S")
elif (abs(a-b) < d < a+b) and (abs(d-b) < a < d+b) and (abs(a-d) < b < a+d):
    print("S")
elif (abs(a-d) < c < a+d) and (abs(c-d) < a < c+d) and (abs(a-c) < d < a+c):
    print("S")
elif (abs(d-b) < c < d+b) and (abs(c-b) < d < c+b) and (abs(d-c) < b < d+c):
    print("S")
else:
    print("N")
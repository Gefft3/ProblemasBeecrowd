n = int(input())
c=0
s1=0
s2=0
while c<n:
    x = int(input())
    if x >= 10 and x <= 20:
        s1+=1
    else:
        s2+=1
    c+=1
print(f"{s1} in\n{s2} out")
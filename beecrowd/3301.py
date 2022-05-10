h, z, l =map(int, input().split())
if (h>z and h<l) or (h<z and h>l):
    print("huguinho")
elif (z>l and z<h) or (z<l and z>h):
    print("zezinho")
else:
    print("luisinho")
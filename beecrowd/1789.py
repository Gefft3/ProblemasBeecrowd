while True:
    try:
        n = int(input())
        l = input().split()
        v = 0
        for i in range(n):
            l[i]=int(l[i])
            if l[i]>v:
                v = l[i]
        if v<10:
            print("1")
        elif v>=10 and v<20:
            print("2")
        elif v>=20:
            print("3")
    except EOFError:
        break
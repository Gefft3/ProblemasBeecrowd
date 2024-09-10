a, b, c = map(int, input().split())


if a > b and b <= c:
    print(':)')
elif a < b and b >= c:
    print(':(')
elif a < b and b < c and (c - b < b - a):
    print(':(')
elif a < b and b < c and (c - b >= b - a):
    print(':)')
elif a > b and b > c and (c - b > b - a):
    print(':)')
elif a > b and b > c and (c - b <= b - a):
    print(':(')
elif a == b:
    if b < c:
        print(':)')
    else:
        print(':(')
 
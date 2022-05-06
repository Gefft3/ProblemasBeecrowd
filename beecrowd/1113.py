x, y = map(int, input().split())
ordem = ""
while x != y:
    if x>y:
        ordem = ordem+"Decrescente\n"
    else:
        ordem = ordem+"Crescente\n"
    x, y = map(int, input().split())

print(ordem.rstrip('\n'))

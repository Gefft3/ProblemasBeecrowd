a, b = map(int, input().split())
fim = 0
if b<=a:
    fim = b-a+24
else:
    fim =b-a
print(f"O JOGO DUROU {fim} HORA(S)")
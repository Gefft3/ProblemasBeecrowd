#problema do sapo
p, q = map(int, input().split())
jump = list(map(int, input().split()))
cnt = 0

for i in range(1, q):
    dif = abs(jump[i] - jump[i-1])
    if dif <= p:
        cnt += 1

if cnt == q - 1:
    print("YOU WIN")
else:
    print("GAME OVER")



     

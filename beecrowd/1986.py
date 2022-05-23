n = int(input())
cod = input().split()
msg = ''
for i in range(n):
    msg += chr(int(cod[i], 16))
print(msg)  
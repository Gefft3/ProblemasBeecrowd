
valores = input().split()
a, b, c = valores

AB = (int(a)+int(b)+abs(int(a)-int(b)))/2 
ABC = (int(AB)+int(c)+abs(int(AB)-int(c)))/2 
print(f"{ABC:.0f} eh o maior")
c,i,j = 0,1,7

while True:
    if i>9:break
    if c == 2:
        print(f"I={i} J={j}")
        i+=2
        j=7
        c=0
    else:
        print(f"I={i} J={j}")
        j-=1
        c+=1
    
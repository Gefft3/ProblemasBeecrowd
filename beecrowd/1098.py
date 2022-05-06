for i in range(0, 22, 2):
    for j in range(10, 31, 10):
        if (i == 0   or  i == 10 or i == 20) and (j == 10 or j == 20 or j==30):
            print(f"I={(i//10)} J={((j+i)//10)}")
        elif i%2==0:
            print(f"I={(i/10)} J={((j+i)/10)}")
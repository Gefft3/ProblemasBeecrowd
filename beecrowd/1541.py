while True:
    try:
        lado_a, lado_b, porcentagem = map(int, input().split())
        area_casa = lado_a * lado_b
    
        metros = 0
        while True:
            aux = metros * metros # area do terreno
            if aux * porcentagem / 100 > area_casa:
                print(metros-1)
                break
            else:
                metros += 1
    except:
        break

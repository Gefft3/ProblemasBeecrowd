numero = input()

parteEsquerda = numero.split(".")[0]
parteDireita = numero.split(".")[1]

print(f"{int(parteDireita)}.{parteEsquerda}")
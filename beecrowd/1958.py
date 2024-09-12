# convertendo para notação científica

entrada = input()

sinal = entrada[0]

if sinal != "-":
    numero = float(entrada)
    print(f"+{numero:.4E}")
else:
    numero = float(entrada[1:])
    print(f"-{numero:.4E}")

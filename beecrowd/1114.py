senha = 2002
lista=""
while True:
    tent = int(input())
    if tent == senha:
        lista+="Acesso Permitido\n"
        break
    else:
        lista+="Senha Invalida\n"
print(lista.rstrip())
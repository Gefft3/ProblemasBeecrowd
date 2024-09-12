# numeração romana para numeros de páginas

def converte(n):
    mapa = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    numeral = ""

    while n > 0:
        for i, r in mapa:
            while n >= i:
                numeral += r
                n -= i

    return numeral


n = int(input())
print(converte(n))

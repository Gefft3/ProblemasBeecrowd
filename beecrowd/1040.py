n1, n2, n3, n4 = map(float, input().split())
media = ((n1*2)+(n2*3)+(n3*4)+(n4))/10

if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media >= 5 and media <= 6.9:
    ex = float(input())
    mediaf = (media+ex)/2
    print(f"Media: {media:.1f}")
    print(f"Aluno em exame.")
    print(f"Nota do exame: {ex:.1f}")
    if mediaf >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {mediaf:.1f}")
    elif mediaf<=4.9:
        print("Aluno reprovado.")
        print(f"Media final: {mediaf:.1f}")
elif media<5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
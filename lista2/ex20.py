nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media == 10:
    print("Aprovado com Distinção!")
elif media >= 7:
    print(f"Aprovado, sua média foi: {media}")
else:
    print(f"Reprovado, sua média foi: {media}")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2)/2
if media >= 9 and media <=10:
    conceito = "A"
elif media < 4:
    conceito = "E"
elif media < 6:
    conceito = "D"
elif media < 7.5:
    conceito = "C"
elif media < 9:
    conceito = "B"

print("Sua nota 1 é: ", nota1)
print("Sua nota 2 é: ", nota2)
print("Sua média é: ", media)
print("Seu conceito é: ", conceito)


if conceito in ["A", "B", "C"]:
    print("APROVADO!")
else:
    print("REPROVADO!")



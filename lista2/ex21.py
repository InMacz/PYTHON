saque = int(input("Digite o valor do saque: "))
if saque < 10 or saque > 600:
    print("Valor minímo é 10 e máximo é 600")
else:
    extenso = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez"]
    resto = saque

    notaCem = resto // 100
    resto = resto%100

    nota50 = resto// 50
    resto = resto%50

    nota10 = resto // 10
    resto = resto% 10

    nota5 = resto //5
    resto = resto%5

    nota1 = resto//1
    partes = []
    if notaCem > 0:
        if notaCem == 1: partes.append(f"{extenso[notaCem]} nota de 100")
        else: partes.append(f"{extenso[notaCem]} notas de 100")
    if nota50 > 0:
        if nota50 == 1: partes.append(f"{extenso[nota50]} nota de 50")
        else: partes.append(f"{extenso[nota50]} notas de 50")
    if nota10 > 0:
        if nota10 == 1: partes.append(f"{extenso[nota10]} nota de 10")
        else: partes.append(f"{extenso[nota10]} notas de 10")
    if nota5 > 0:
        if nota5 == 1: partes.append(f"{extenso[nota5]} nota de 5")
        else: partes.append(f"{extenso[nota5]} notas de 5")
    if nota1 > 0:
        if nota1 == 1: partes.append(f"{extenso[nota1]} nota de 1")
        else: partes.append(f"{extenso[nota1]} notas de 1")
frase = ", ".join(partes[:-1]) + " e " + partes[-1]
print(f"Para sacar {saque} reais, o programa fornece {frase}.")

numero = int(input("Digite um número entre 1 e 999: "))
if numero > 999 or numero < 1:
    print("Valor inválido!")
    exit()

centena = numero // 100
dezena = (numero % 100)// 10
unidade = numero%10

if centena != 1:
    msgCentena = "centenas"
else:
    msgCentena = "centena"

if dezena != 1:
    msgDezena = "dezenas"
else:
    msgDezena = "dezena"

if unidade != 1:
    msgUnidade = "unidades"
else:
    msgUnidade = "unidade"

partes = []
if centena > 0:
    partes.append(f"{centena} {msgCentena}")
if dezena > 0:
    partes.append(f"{dezena} {msgDezena}")
if unidade > 0:
    partes.append(f"{unidade} {msgUnidade}")

if len(partes) == 1:
    resultado = partes[0]
elif len(partes) == 2:
    resultado = partes[0] + " e " + partes[1]
elif len(partes) == 3:
    resultado = partes[0] + ", " + partes[1] + " e " + partes[2]

print(f"{numero} = {resultado}")

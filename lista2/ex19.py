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

print(f"{numero} = {centena} {msgCentena}, {dezena} {msgDezena} e {unidade} {msgUnidade}")

combustivel = input("Qual tipo de combústivel vai colocar? A - Álcool ou G - Gasolina: ") 
if combustivel.upper() != "A" and combustivel.upper() != "G":
    print("Combustível inválido! ")
    exit()
litros = float(input("Quantos litros: "))
precoLitroG = 2.5
precoLitroA = 1.9
if combustivel.upper() == "A":
    if litros <= 20:
        precoDesconto = precoLitroA - (precoLitroA*3)/100
    else:
        precoDesconto = precoLitroA - (precoLitroA*5)/100
elif combustivel.upper() == "G":
    if litros <= 20:
        precoDesconto = precoLitroG - (precoLitroG*4)/100
    else:
        precoDesconto = precoLitroG - (precoLitroG*6)/100
valorTotal = precoDesconto * litros



print(f"Valor a ser pago em {litros} litros é: {precoDesconto:.2f} por litro, valor total: R${valorTotal:.2f}")
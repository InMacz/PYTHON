tipoCarne = (input("Digite o tipo da carne, File Duplo, Alcatra ou Picanha: F / A / P: "))
if tipoCarne.upper() != "F" and tipoCarne.upper() != "A" and tipoCarne.upper() != "P":
    print("Carne inválida!")
    exit()

kgCarne = float(input("Digite em Kg da carne: "))

if tipoCarne.upper() == "F":
    tipoCarneTexto = "File Duplo"
    if kgCarne <= 5:
        precoCarne = kgCarne * 4.9
    else:
        precoCarne = kgCarne * 5.8

elif tipoCarne.upper() == "A":
    tipoCarneTexto = "Alcatra"
    if kgCarne <= 5:
        precoCarne = kgCarne * 5.9
    else:
        precoCarne = kgCarne * 6.8

elif tipoCarne.upper() == "P":
    tipoCarneTexto = "Picanha"
    if kgCarne <= 5:
        precoCarne = kgCarne * 6.9
    else:
        precoCarne = kgCarne * 7.8
    

tipoPagamento = input("Vai pagar com cartão Tabajara? S / N: ")
if tipoPagamento.upper() == "S":
    desconto = (precoCarne*5)/100
    precoDesconto = precoCarne-desconto
elif tipoPagamento.upper() == "N":
    desconto = 0
    precoDesconto = precoCarne
else:
    print("Digite S ou N!")
    exit()



print(f"Tipo da carne: {tipoCarneTexto}, quantidade: {kgCarne} KG, preço total: R${precoCarne:.2f}, Tipo de pagamento: {'Cartão Tabajara' if tipoPagamento.upper() == 'S' else 'Outro'}, desconto: R${desconto:.2f}, valor a pagar: {precoDesconto:.2f}")




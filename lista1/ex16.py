import math
metros = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
litroTinta = metros/3
lataTinta = math.ceil(litroTinta/18)
precoTinta = lataTinta*80
print("Você terá que comprar", lataTinta, "latas de tinta e ficará no preço de:", precoTinta, "R$")

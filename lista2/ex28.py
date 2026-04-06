kgMorango = float(input("Digite em Kg a quantidade de Morangos: "))
kgMaca = float(input("Digite em Kg a quantidade de Maçãs: "))
if kgMorango <= 5:
    precoMorango = kgMorango * 2.5
else:
    precoMorango = kgMorango * 2.2
if kgMaca <= 5:
    precoMaca = kgMaca * 1.8
else:
    precoMaca = kgMaca * 1.5

totalPreco = precoMaca + precoMorango
totalKg = kgMaca + kgMorango

if totalPreco > 25 or totalKg > 8:
    totalPreco = totalPreco - (totalPreco*10)/100

print(f"Valor á ser pago será de: R$ {totalPreco:.2f}")
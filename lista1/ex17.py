import math
metros = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
litrosNecessarios = (metros/6) * 1.10
latasApenas = math.ceil(litrosNecessarios/18)
galoesApenas = math.ceil(litrosNecessarios/3.6)
latasNaMistura = math.floor(litrosNecessarios/18)
litrosSobrando = litrosNecessarios - (latasNaMistura * 18)
galoesNaMistura = math.ceil(litrosSobrando/3.6)
precoLataMistura = latasNaMistura*80
precoGalaoNamistura = galoesNaMistura*25
precoMistura = precoLataMistura + precoGalaoNamistura

precoApenasGalao = galoesApenas * 25
precoApenasLata = latasApenas * 80
print("Você terá que comprar", latasApenas, "latas de tinta e ficará no preço de:", precoApenasLata, "R$")
print("Você terá que comprar", galoesApenas, "galões de tinta e ficará no preço de:", precoApenasGalao, "R$")
print("Se misturar os dois serão ", latasNaMistura, "latas ", galoesNaMistura, "galões, e o preço ficará de: ", precoMistura, "R$")
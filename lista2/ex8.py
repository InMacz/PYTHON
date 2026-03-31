produto1 = float(input("Digite o preço do produto 1: "))
produto2 = float(input("Digite o preço do produto 2: "))
produto3 = float(input("Digite o preço do produto 3: "))
if produto1 < produto2 and produto1 < produto3:
    print("Compre o produto 1, ele é mais barato!")
elif produto2 < produto1 and produto2 < produto3:
    print("Compre o produto 2, ele é mais barato!")
elif produto3 < produto1 and produto3 < produto2:
    print("Compre o produto 3, ele é mais barato!")
else:
    print("Itens com mesmo valor, escolha como quiser!")
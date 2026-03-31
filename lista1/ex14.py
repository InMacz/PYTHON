peso = float(input("Digite em KG o peso dos peixes: "))
excesso = peso-50
multa = excesso*4
if peso > 50:
    print("Sua multa ficou R$", multa, "reais")
else:
    print("Multa não aplicada")
    
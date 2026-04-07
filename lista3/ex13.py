base = float(input("Digite o número para a base: "))
expoente = int(input("Digite o número para o expoente: "))
resultado = 1
for i in range(expoente):
    resultado = resultado * base
print(resultado)



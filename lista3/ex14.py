quantidade = 10
impar = 0
par = 0
for i in range(quantidade):
    numero = int(input(f"Digite o número {i+1}: "))
    if numero%2 != 0:
        impar += 1
    else:
        par += 1

print(f"IMPARES: {impar}")
print(f"PARES: {par}")

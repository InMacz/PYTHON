maior = float(input("Digite o número 1: "))
for i in range(1, 5):
    numero = float(input(f"Digite o número {i+1}: "))
    if numero > maior:
        maior = numero
    
print(f"Maior número é: {maior}")
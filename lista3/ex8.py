soma = 0
quantidade = 5
for i in range(quantidade):
    numero = float(input(f"Digite o número {i+1}: "))
    soma += numero

media = soma/quantidade
    
print(f"SOMA: {soma}")
print(f"MEDIA: {media}")
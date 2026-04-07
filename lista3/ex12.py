while True:
    numero = int(input("Digite a tabua desejada entre 1 e 10: "))
    if numero > 10 or numero < 1:
        print("Deve ser entre 1 e 10!")
    else:
        break
    
print(f"Tabuada de {numero}: ")
for i in range(1, 11):
    print(f"{numero} X {i} = {i*numero}")


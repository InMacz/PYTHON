while True:
    while True:
        popA = int(input("Digite a população de A: "))
        if popA <= 0:
            print("População deve ser maior que zero!")
        else:
            break

    while True:
        popB = int(input("Digite a população de B: "))
        if popB <= 0:
            print("Populaçao deve ser maior que zero!")
        elif popB <= popA:
            print("População B deve ser maior que A!")
        else:
            break

    while True:
        taxaA = float(input("Informe a taxa de A: "))
        taxaB = float(input("Informe a taxa de B: "))
        if taxaA <= 0 or taxaB <= 0:
            print("As taxas devem ser maiores que zero!")
        elif taxaA <= taxaB:
            print("Taxa A deve ser maior que taxa B para A alcançar B!")
        else:
            break
    anos = 0
    while popA < popB:
        popA += (popA*taxaA)/100
        popB += (popB*taxaB)/100
        anos += 1
  
    print(f"Irá demorar {anos} anos para popA passar popB")
    print(f"População A: {popA:.2f}")
    print(f"População B: {popB:.2f}")

    respota = input("Deseja calcular novamente? (s/n): ")
    if respota.lower() != "s":
        break
print("Encerrando o programa!")
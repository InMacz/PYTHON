lado1 = float(input("Digite o lado 1 do triângulo: "))
lado2 = float(input("Digite o lado 2 do triângulo: "))
lado3 = float(input("Digite o lado 3 do triângulo: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:

    if  lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("Triângulo Isósceles")
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print("Triângulo Escaleno")
    
else:
    print("Valores inválidos")
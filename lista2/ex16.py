#ax2 + bx + c
import sys
import math
a = float(input("Digite o valor de A: "))
if a == 0:
    print("Valor inválido, não é uma equação de segundo grau! ")
    sys.exit()


b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = (b*b) - 4*a*c

if delta < 0:
    print("Equação não possui raízes!")
    sys.exit()

elif delta == 0:
    raiz = (-b) / (2*a)
    print("Apenas uma raiz real: ", raiz)
else:
    raiz1 = ((-b) + math.sqrt(delta))/(2*a)
    raiz2 = ((-b) - math.sqrt(delta))/(2*a)
    print("Raiz 1: ", raiz1)
    print("Raiz 2: ", raiz2)


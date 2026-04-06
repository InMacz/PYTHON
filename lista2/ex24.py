num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
operacao = input("Informe a operação desejada: + - * ou /")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Erro: divisão por zero!")
        exit()
    resultado = num1 / num2
else:
    print("Operação inválida!")
    exit()


print(resultado)

if resultado == round(resultado):
    if int(resultado) % 2 == 0:
        print("Número é par!")
    else:
        print("Número é ímpar!")
else:
    print("O número é decimal, par/impar não se aplica.")


if resultado > 0:
    print("Número positivo")
elif resultado == 0:
    print("Número é 0")
else:
    print("Número é negativo!")


if resultado == round(resultado):
    print("Número inteiro!")
else:
    print("Número decimal!")


num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))
num3 = int(input("Digite o número 3: "))
if num1 > num2 and num1 > num3:
    print(num1, "é o maior")
elif num2> num1 and num2>num3:
    print(num2, "é o maior")
elif num3 > num2 and num3>num1:
    print(num3, "é o maior")
else:
    print("empate")
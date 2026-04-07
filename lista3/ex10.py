num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))
for i in range(min(num1, num2), max(num1, num2)+1):
    print(i)
a = 1
b = 1
termo = int(input("Digite o termo Fibonacci: "))
if termo == 1:
    print (a)
elif termo == 2:
    print (a)
    print(b)
elif termo > 2:
    print (a)
    print(b)
    for i in range(termo-2):
        soma = a+b
        print(soma)
        a = b
        b = soma
else:
    print("Deve ser maior que 0! ")
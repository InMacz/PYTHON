salario = int(input("Digite seu salário atual: "))


if salario <= 280:
    porcentagem = 20
elif salario > 280 and salario < 700:
    porcentagem = 15
elif salario > 700 and salario < 1500:
    porcentagem = 10
elif salario >= 1500:
    porcentagem = 5
    

salarioReajuste = salario + (salario*porcentagem)/100
aumento = salarioReajuste - salario 

print("Seu salário antigo era: ", salario, "R$")
print("Percentual de aumento aplicado: ", porcentagem, "%")
print("Seu aumento foi de: ", aumento, "R$")
print("Seu novo salário agora é: ", salarioReajuste, "R$")
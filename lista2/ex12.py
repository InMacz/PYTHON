ganhoHora = float(input("Quanto você ganha por hora: "))
horasTrabalhadas = float(input("Quantas horas trabalha no mês: "))

salarioBruto = ganhoHora * horasTrabalhadas
if salarioBruto < 900:
    porcentagem = 0
elif salarioBruto < 1500:
    porcentagem = 5
elif salarioBruto < 2500:
    porcentagem = 10
else:
    porcentagem = 20

ImpostoRenda = (salarioBruto*porcentagem)/100
inss = (salarioBruto*10)/100
fgts = (salarioBruto*11)/100
salarioLiquido = salarioBruto - ImpostoRenda - inss
print("Salário Bruto: ", salarioBruto)
print("Imposto de renda: ", ImpostoRenda)
print("INSS: ", inss)
print("FGTS: ", fgts)
print("Total de descontos: ", salarioBruto - salarioLiquido)
print("Salário Liquido: ", salarioLiquido)
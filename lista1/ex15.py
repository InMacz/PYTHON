ganhoHora = float(input("Quanto você ganha por hora: "))
horasTrabalhadas = float(input("Quantas horas trabalha no mês: "))
salarioBruto = ganhoHora * horasTrabalhadas
ImpostoRenda = (salarioBruto*11)/100
inss = (salarioBruto*8)/100
sindicato = (salarioBruto*5)/100
salarioLiquido = salarioBruto - ImpostoRenda - inss - sindicato
print("Salário Bruto: ", salarioBruto)
print("Imposto de renda: ", ImpostoRenda)
print("INSS: ", inss)
print("Sindicato: ", sindicato)
print("Salário Liquido: ", salarioLiquido)
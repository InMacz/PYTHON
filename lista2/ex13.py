diasSemana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
dia = int(input("Digite o dia em número de 1 a 7: "))


if dia>= 1 and dia <= len(diasSemana):
    print("Dia escolhido: ", diasSemana[dia - 1])
else:
    print("Digite um valor válido!")


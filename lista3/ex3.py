while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        print("Nome registrado com sucesso!")
    else:
        print("Nome deve ter mais de 3 caracteres!")
        continue
    break

while True:
    idade = int(input("Digite sua idade: "))
    if idade > 0 and idade < 150:
        print("Idade computada com sucesso!")
    else:
        print("Digite uma idade entre 0 e 150!")
        continue
    break

while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        print("Salário computado com sucesso!")
    else:
        print("Salário deve ser maior que 0!")
        continue
    break

while True:
    sexo = input("Digite seu sexo, sendo F para Feminino e M para Masculino: ")
    if sexo.upper() == "F":
        print("Sexo Feminino computado!")
    elif sexo.upper() == "M":
        print("Sexo Masculino computado!")
    else:
        print("Sexo inválido!")
        continue
    break

while True:
    estadoCivil = input("Digite seu Estado Civil, sendo S, C, V, D: ")
    if estadoCivil.upper() == "S" or estadoCivil.upper() == "C" or estadoCivil.upper() == "V" or estadoCivil.upper() == "D":
        print("Estado Civil computado!")
    else:
        print("Digite Estado Civil válido!")
        continue
    break

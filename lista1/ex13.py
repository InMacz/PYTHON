
sexo = input("Digite seu gênero: ")

if sexo.upper() == "F":
        altura = float(input("Digite sua altura: "))
        pesoIdealMulher = (62.1*altura)-44.7
        print("Seu peso ideal é: ", pesoIdealMulher)
elif sexo.upper() == "M":
        altura = float(input("Digite sua altura: "))
        pesoIdealHomem = (72.7*altura)-58
        print("Seu peso ideal é: ", pesoIdealHomem)
else:
        print("Sexo inválido")
pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

contador = 0
if pergunta1 == "sim":
    contador += 1
elif pergunta1 != "não":
    print("Resposta inválida!")
    exit()

if pergunta2 == "sim":
    contador +=1
elif pergunta2 != "não":
    print("Resposta inválida")
    exit()

if pergunta3 == "sim":
    contador +=1
elif pergunta3 != "não":
    print("Resposta inválida")
    exit()

if pergunta4 == "sim":
    contador +=1
elif pergunta4 != "não":
    print("Resposta inválida")
    exit()

if pergunta5 == "sim":
    contador +=1
elif pergunta5 != "não":
    print("Resposta inválida")
    exit()
   
if contador == 5:
    classificacao = "Assassino"
elif contador >= 3:
    classificacao = "Cúmplice"
elif contador == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

print(classificacao)
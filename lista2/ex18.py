dia = int(input("Informe o dia: "))
if dia > 31 or dia < 1:
    print("Data inválida!")
    exit()

mes = int(input("Informe o mes: "))
if mes > 12 or mes < 1:
    print("Data inválida!")
    exit()
if dia == 31  and mes in (2, 4, 6, 9, 11):
    print("Data inválida!")
    exit()
elif dia == 30 and mes in (1, 2, 3, 5, 7, 8, 10, 12):
    print("Data inválida!")
    exit()
ano = int(input("Informe o ano: "))

if dia == 29 and mes == 2:
    if (ano%4 == 0 and (ano%400 == 0 or ano%100 != 0)):
        print(f"{dia}/{mes}/{ano}")
    else:
        print("Data inválida!")
        exit()
else:
    print(f"{dia}/{mes}/{ano}") 
        
 




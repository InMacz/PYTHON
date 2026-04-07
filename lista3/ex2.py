while True:
    nome = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    if senha != nome:
        print("Informações armazenadas com sucesso!")
        break
    else:
        print("Senha deve ser difirente do Usuário!")
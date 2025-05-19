import inputs

reuniao = []
presente = []
ausente = []

while True:
    print("")
    print("[1] Cadastro dos pais ")
    print("[2] Exibir o total de pais ")
    print("[3] Lista em ordem alfabética ")
    print("[4] Confirmação de presença dos pais ")
    print("[5] Relatório de pais presentes e ausentes ")
    print("[6] sair ")
    escolha = inputs.input_int("Escolha uma das opções ")
    print("")
   
    if escolha == 1:
        nome = inputs.input_str("Digite o nome ")
        print("")
        if nome in reuniao:
            print("Este nome já está na lista")
            print("")
        else:
            reuniao.append(nome)
            print("Adicionado")
    elif escolha == 2:
            print(" A lista tem", len(reuniao ))
    elif escolha == 3:
        reuniao.sort()
        for nome in reuniao:
            print(nome)
    elif escolha == 4:
        for nome in reuniao:
            print(nome)
            consulta = inputs.input_str("Está presente? S/n ")
            print("")
            if  consulta == "Sim":
                presente.append(nome)
                print("Está presente")
            else:
                ausente.append(nome)
                print("Está ausente")
    elif escolha == 5:
        print("Pais presentes na reunião ")
        for nome in presente:
            print(nome)
            print("")
        print("Pais ausentes na reunião ")
        for nome in ausente:
            print(nome)
            print("")
    elif escolha == 6:
            print("sair")
            break 


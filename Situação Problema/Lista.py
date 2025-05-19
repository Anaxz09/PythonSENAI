nomes = []

while True:
    print("")
    print("[1] Cadastrar nome ")
    print("[2] Verificar a quantidade de nomes na lista ")
    print("[3] Exibir a lista de nomes em ordem alfabética ")
    print("[4] Consulta de um nome ")
    escolha = int(input("Escolha uma das opções "))
    print("")
    
    if escolha == 1:
        nome = input("Digite seu nome ")
        print("")
        if nome in nomes:
            print("Este nome já está na lista")
        else:
            nomes.append(nome)
            print("Seu nome foi adicionado com sucesso")
    elif escolha == 2:
        print("A lista tem", len(nomes ))
    elif escolha == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
    elif escolha == 4:
        consulta_nome = input("Consultar  nome ")
        print("")
        if consulta_nome in nomes:
            op = input("Nome encontrado! Deseja removê-lo? (s/n) ")
            if op == "Sim":
                nomes.remove (consulta_nome)
                print("Nome removido com sucesso")
        else:
            op1 = input("Nome não encontrado. Deseja adicioná-lo? (s/n) ")
            if op1 == "Sim":
                nomes.append(consulta_nome)
                print("Nome adicionada a lista com sucesso")
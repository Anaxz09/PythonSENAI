def verificar_ar():
    while True:
        print()
        print("\033[33;1mMenu\033[ m")
        print("Esta inverno ou verão?")
        print("[1] - Inverno")
        print("[2] - Verão")
        print("")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            inv = int(input("Qual é a temperatura no inverno?: "))
            umi = int(input("Qual é a sua umidade no inverno?: "))
            print()
            
            if umi > 40 and umi <= 55:
                print("A umidade está ideal no inverno")
            else:
                print("A umidade não está ideal no inverno")
            
            if inv > 20 and inv <= 22:
                print("A temperatura está ideal no inverno")
            else:
                print("A temperatura não está ideal no inverno")
            
        else:
            ver = int(input("Qual é a temperatura no verão?: "))
            umi1 = int(input("Qual é a sua umidade no verão?: "))
            print()
            
            if umi1 > 40 and umi1 <= 55:
                print("A umidade está ideal no verão")
            else:
                print("A umidade não está ideal no verão")
            
            if ver > 20 and ver <= 22:
                print("A temperatura está ideal no verão")
            else:
                print("A temperatura não está ideal no verão")
            
        
            
verificar_ar()          

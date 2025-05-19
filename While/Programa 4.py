while True:
    print("Escolha uma opção ")
    print("menu ")
    print("[0] - Sair")
    print("[1] - Fatorial ")
    print("[2] - Quadrado ")
    print("[3] - Cubo ")
    print("[4] - Tabuada ")
    escolha = int(input("escolha um número "))
    if escolha == 0:
        print("sair ")
        break
    elif escolha == 1:
        num2 = int(input("Digite um número "))
        n = num2
        while n > 1:
            n = n - 1
            num2 = num2 * n
        print("O fatorial é ", num2)
           
           
    elif escolha == 2:
        num = int(input("Digite um número "))
        resultado = num * num
        print("O quadrado desse número é ", resultado)
    elif escolha == 3:
        num1 = int(input("Digite um número "))
        resultado = num1 * num1 * num1
        print("O cubo desse número é ", resultado)
    elif escolha == 4:
        num2 = int(input("Digite um número "))
        print(num2, "X 1 = ", num1 * 1)
        print(num2, "X 2 = ", num1 * 2)
        print(num2, "X 3 = ", num1 * 3)
        print(num2, "X 4 = ", num1 * 4)
        print(num2, "X 5 = ", num1 * 5)
        print(num2, "X 6 = ", num1 * 6)
        print(num2, "X 7 = ", num1 * 7)
        print(num2, "X 8 = ", num1 * 8)
        print(num2, "X 9 = ", num1 * 9)
        print(num2, "X 10 = ", num1 * 10)

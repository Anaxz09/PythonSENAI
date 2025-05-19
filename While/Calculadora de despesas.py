quantidade = 0
valor_total = 0

while True:
    print("Escolha uma opção ")
    print("menu ")
    print("[0] - sair ")
    print("[1] - mostrar a quantidade e o valor total das despesas ")
    print("[2] - adicionar valor da despesa ")
    escolha = int(input("escolha um número "))
    if escolha == 0:
        print("Sair ")
        break
    elif escolha == 1:
        print("a quantidade é ", quantidade, "e o valor total é ", valor_total )
    elif escolha == 2:
        valor = int(input("digite um valor de despesa "))
        quantidade = quantidade + 1
        valor_total = valor_total + valor

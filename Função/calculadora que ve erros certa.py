def menu_calculadora():
    while True:
        print("\033[33;1mMenu\033[ m")
        print("")
        print("[1] - \033[34;1mAdição\033[ m")
        print("[2] - \033[34;1mSubtração\033[ m")
        print("[3] - \033[34;1mMultiplicação\033[ m")
        print("[4] - \033[34;1mDivisão\033[ m")
        print("[5] - \033[34;1mTodas as operações\033[ m")
        print("[6] - \033[34;1mSair\033[m")
        while True:
            try:
                opcao = int(input("\033[33;1mEscolha um número\033[ m "))
                break
            
            except ValueError:
                print("\033[31;1mDigite somente números ex:6\033[m")
        if opcao != 6:
            while True:
                try:
                    num1 = float(input("\033[35;1mDigite um número\033[m "))
                    break
                
                except ValueError:
                    print("\033[31;1mDigite somente números ex:6\033[m")
                    
            while True:
                try:
                    num2 = float(input("\033[35;1mDigite outro número\033[m "))
                    break
                except ValueError:
                    print("\033[31;1mDigite somente números ex:6\033[m")
             
        if opcao == 1:
            print("\033[32;1mO resultado da adição é\033[m" , soma(num1,num2))
        elif opcao == 2:
            print("\033[32;1mO resultado da subtração é\033[m" , subtração(num1,num2))
        elif opcao == 3:
            print("\033[32;1mO resultado da multiplicação é\033[m" , multiplicação(num1,num2))
        elif opcao == 4:
            print("\033[32;1mO resultado da divisão é\033[m" , divisão(num1,num2))
        elif opcao == 5:
            resultados(num1,num2)
        elif opcao == 6:
            print("sair")
            break
        
        else:
            print("invalido")
                   
def soma(num1,num2 ):
    return num1 + num2

def subtração(num1,num2):
    return num1 - num2

def multiplicação(num1,num2):
    return num1 * num2

def divisão (num1,num2):
    return num1 / num2

def resultados(num1,num2):
    print(soma (num1,num2), "É o resultado da adição")
    print(subtração (num1,num2), "É o resultado da subtração")
    print(multiplicação (num1,num2), "É o resultado da multiplicação")
    print(divisão (num1,num2), "É o resultado da divisão")


menu_calculadora()
import random

#Fazer o jogo Par ou Ímpar
#Nome do Jogo: Vamos jogar?
#Fazer uma instrução para o jogar(o que é o jogo e como joga)
#Pedir para o usuario escolher par ou impar e um numero
#Mostrar o resultado e quem ganhou
#Perguntar se deseja continuar o sair

print("\033[1;35mBem-vindo ao jogo: Par ou Ímpar!!\033[m")
print("")
print("°Esse jogo e composto pela seguinte regra:")
print("Você pode escolher se quer ser par ou ímpar, seu oponete, que será eu, a Pithy, ficará com o que sobrou.")
print("Logo em seguida, você escolherá e digitará um número de 1 a 5, eu, Pithy, também escolherá, e no final vemos quem ganhou!!")
print("")
print("*Você so ganha quando o número que sai é a soma de um número da sua escolha, como par ou ímpar!!")
print("")


print("")

while True:
    print("Vem, vamos jogar!, caso não queira, está tudo bem")
    print("Escolha o que você quer ser?")
    print("")
    print("[1] Par")
    print("[2] Ímpar")
    print("[3] Sair")
    print("")
    num = int(input("Escolha um número: "))
    print("")
    
    if num == 3:
        print("Obrigada por jogar!! ;)")
        break

    jog = int(input("Digite um número de 1 a 5: "))
    phity = random.randint(1, 5)

    print("Seu número", jog)
    print("Meu número", phity)

    soma = jog + phity
    print("O resultado é", soma)

    if soma % 2 == 0:
        if num == 1:
            print("Você ganhou, parabéns!")
        else:
            print("Você perdeu, mais sorte na proxima vez ;)")
    else:
        print("")
        
        if num == 2:
            print("Você ganhou, parabéns")
        else:
            print("Você perdeu, mais sorte na proxima vez ;)")
        
            
        

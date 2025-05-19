import random
#Jogo de adivinhação
#Fazer uma instrução para o jogar(o que é o jogo e como joga)

print("\033[1;35mBem-vindo de volta, jogador!!\033[m")
print("O jogo de hoje é Adivinhação!")
print("")
print("\033[33mEsse jogo e composto pela seguinte regra:\033[m")
print("Eu, \033[1;36mPithy\033[m, escolherei um número, e \033[1;35mvocê\033[m, terá que advinhar esse número. É bem simples!")
print("A cada chute do seu, irei mostrar uma mensagem se o chute está maior ou menor do que o número misterioso :)")
print("")
print("\033[31mVocê só ganha quando você acertar o número!!\033[m")
print("\033[34mBoa sorte ;)!!\033[m")
print("")

print("Podemos começar?")
print("")
print("[1] \033[33mSim\033[m")
print("[2] \033[31mNão\033[m")
print("")
num = int(input("Escolha um número: "))
print("")

phity = random.randint(1, 100)
while True:
    
    
    if num == 2:
        print("Até a próxima jogador!! ;)")
        break
    
    if num == 1:
        print("")
        
        n = int(input("Tente adivinhar o número misterioso: "))
        
        print("")
        
        if n > phity:
            print("Não, o número misterior é menor")
        elif n < phity:
            print("Não, o número misterior é maior")
        else:
            print("Acertou! O número misterioso é", phity)
            print("Deseja continuar?")
            print("")
            print("[1] Sim!!")
            print("[2] Não, obrigado!")
            print("")
            num1 = int(input("Escolha uma dessas opções: "))
            
            print("")
            
            if num1 == 1:
                print("Ótimo, vamos começar de novo!!")
                phity = random.randint(1, 100)
                
                print("")
            
            else:
                print("Que pena, até a proxima jogador ;)")
                break
        
        
    
    
    
    
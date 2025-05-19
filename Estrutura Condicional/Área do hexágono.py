#1. Criem um algoritmo sequencial explicando passo a passo o processo de cálculo da área.

#2. Implementem o código do programa em Python.

#3. Expliquem como o programa deve ser utilizado, incluindo exemplos claros de entrada e
#saída, para que qualquer pessoa possa entender como usá-lo.

#Equação: At: l² . 3**0,5
#               / 4

#Passo 1:Escolha um número
#Passo 2:Faça a raiz de três
#Passo 3:Multiplique o número escolhido por ele mesmo
#Passo 4:Multiplique o resultado da raiz pela multiplicação do número escolhido
#Passo 5:Divide a multiplicação por quatro

#2 equação: Ah: 6 * At

num1 = int(input("Digite um número "))

mult = num1 * num1
raiz = round(3**0.5, 2) * mult
divisão = raiz / 4
area = 6 * divisão
print("A área do hexágono vai ser " + str(area))


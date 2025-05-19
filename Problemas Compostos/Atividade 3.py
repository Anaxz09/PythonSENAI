#capacidade maxima: 50 litros
#quantidade de litros atual: 20 litros
#quantidade restante: 30 litros
#custo atual da gasolina: R$5,80

#1- quantos reias vai ficar quando completar o tanque

#2- o preço do combustível, a capacidade maxima, a quantidade atual

#3-
# A. a capacidade maxima menos a quantidade atual
# B. ter o resultado da quantidade que falta
# C. fazer a quantidade de falta vezes o preço da gasolina
# D. obter o resultado

num1 = 50
num2 = 20
num3 = 5.80

sub = num1 - num2
multiplicaçao = sub * num3
print("A quantidade que falta para completar o tanque é " + str(sub))
print("O preço da gasolina é " + str(multiplicaçao))

#Digite seus numeros

num1 = int(input("Digite sua capacidade máxima "))
num2 = int(input("Digite a quantidade de combustível do seu veículo "))

sub = num1 - num2

print("A quantidade que falta para completar o tanque é " + str(sub))

num3 = float(input("Digite o preço do combustível "))

multiplicação = sub * num3

print("O preço ficou " + str(multiplicação))





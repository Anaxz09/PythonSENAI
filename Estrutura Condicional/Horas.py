#Escolha uma hora
#Fazer a conversão de hora para segundos
#Passo 1: Hora escolhida / por 60
#Depois fazer a conversão de minutos para segundos
#Passo 2: A resposta * 60

num1 = int(input("Digite a hora "))

min = num1 * 60
seg = min * 60

print("Os minutos vão ser " + str(min))
print("Os segundos vão ser " + str(seg))

# Solicite dois números
# Escolher uma operação matemática
# Se o usuário inserir uma operação inválida, deve informar que é desconhecida
# Se não, deve aparecer o resultado

num1 = int(input("Digite um número "))
num2 = int(input("Digite outro número "))
num3 = input("Digite uma operação matemática " )

op_mais = ("+")
op_menos = ("-")
op_divisao = ("/")
op_mult = ("*")

op_mat = ("+, -, *, /")

mais = num1 + num2
menos = num1 - num2
mult = num1 * num2
divisao = num1 / num2

if num3 == op_mais:
    print("O resultado vai ser " , mais)

elif num3 == op_menos:
    print("O resultado vai ser " , menos)
    
elif num3 == op_divisao:
    print("O resultado vai ser " , divisao)
    
elif num3 == op_mult:
    print("O resultado vai ser " , mult)

else:
    print("A operação desconhecida")

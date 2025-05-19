# Solicite duas notas
# calcule a média
# 70 = aprovado
# 50 e 70 = recuperação
# 50 = reprovado

num1 = int(input("Digite uma nota "))
num2 = int(input("Digite outra nota "))

media = num1 + num2
divisao = media / 2

if divisao >= 70 and divisao == 100:
    print("Aprovado")
    
elif divisao >= 50 and divisao <= 70:
    print("Recuperação")
    
else:
    print("Reprovado")


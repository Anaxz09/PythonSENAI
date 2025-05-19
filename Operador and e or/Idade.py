# Solicite  o ano de nascimento
# calcular a idade
# verificar a faixa etaria da criança
# abaixo de 10 = criança
# de 11 a 17 = adolescente
# de 18 a 59 = adulto
# acima de 60 = idoso

num1 = int(input("Digite o ano do seu nascimento "))
num2 = int(input("Digite o ano atual "))

sub = num2 - num1

if sub > 0 or sub == 100:
    if sub >= 10 and sub == 10:
        print("Criança")
    
    elif sub >= 11 and sub <= 17:
        print("Adolescente")
    
    elif sub >= 18 and sub <= 59:
        print("Adulto")
    
    else:
        print("Idoso")
        
        
        




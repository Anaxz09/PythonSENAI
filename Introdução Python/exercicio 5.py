#solicitar um numero de 1 a 7
#digitar qual o dia da semana relacionado

num1 = int(input("Digite um numero de 1 a 7 "))

dia = (1, 2, 3, 4, 5, 6, 7)

if num1 == 1:
    print("É Domingo")
   
elif num1 == 2:
    print("É Segunda-Feira")
   
elif num1 == 3:
    print("É Terça-Feira")
   
elif num1 == 4:
    print("É Quarta-Feira")
   
elif num1 == 5:
    print("É Quinta-Feira")
   
elif num1 == 6:
    print("É Sexta-Feira")
   
else:
    print("É Sábado")
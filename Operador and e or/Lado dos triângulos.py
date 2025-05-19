# fale os lados dos triangulo
# se for equilatero, e todos os lados iguais
# se for isosceles, e dois lado iguais e o terceiro e diferente
# e se for escaleno, os tres lados são diferentes

num1 = input("Digite um lado ")
num2 = input("Digite o outro lado ")
num3 = input("Digite o último lado ")

if num1 == num2 and num2 == num3:
    print("Equilátero")
    
elif num1 == num2 and num2 != num3 or num1 == num3 and num2 != num3 or num1!= num2 and num2 == num3:
    print("Isósceles")
    
else:
    print("Escaleno")


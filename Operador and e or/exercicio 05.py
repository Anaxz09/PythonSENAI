#solicite um numero
#solicite outro numero
#solicite outro numero
#compare qual numero é maior

num1 = int(input("Digite um numero "))
num2 = int(input("Digite um numero diferente "))
num3 = int(input("Digite mais um numero "))


if num1 > num2:
    if num1 > num3:
        print("o primeiro é maior ")
    elif num3 > num2:
        print("o terceiro é maior ")
elif num2 > num3:
    print("o segundo é maior ")
elif num3 > num1:
    print("o terceiro é maior ")
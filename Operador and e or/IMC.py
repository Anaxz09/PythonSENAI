# indique seu peso
# sua altura
# Calcular o IMC
# escala, abaixo do peso, peso normal, sobrepeso e obesidade

num1 = float(input("Digite seu altura "))
num2 = float(input("Digite sua peso "))

mult = round(num1 * num1, 2 )
imc = round(num2 / mult, 2 )

if imc <= 18.5:
    print("Magreza")
    
elif imc > 18.5 and imc <= 24.9:
    print("Normal")

elif imc > 25 and imc <= 29.9:
    print("Sobrepeso")
    
elif imc > 30 and imc <= 34.9:
    print("Obesidade grau I")

elif imc > 35 and imc <= 39.9:
    print("Obesidade grau II")
    
elif imc > 40 :
    print("Obesidade grau III")




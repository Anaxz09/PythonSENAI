def calculo_fahrenheit(celsius):
    return celsius * 1.8 + 32
  

def calculo_kelvin(celsius):
    return celsius + 273
    
temperatura = float(input("Digite a temperatura "))

print("Temperatura do fahrenheit", calculo_fahrenheit(temperatura))
print("Temperatura do kelvin", calculo_kelvin(temperatura))

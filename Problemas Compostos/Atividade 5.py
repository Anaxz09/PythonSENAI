#Preço do combustivel: 6,90
#O carro tem: 10 litros no tanque
#O carro tem uma autonomia de 7 km
#Viagem vale: 800 km
#O carro ja percorreu: 90 km

#1- Quantos litro de combustivel e quantos reais para fazer uma viagem
#2- os km que vai percorrer, 

l1 = int(800 - 90)
l2 = int(l1 / 7)
v1 = int(l2 - 10)
v2 = int(v1 * 6.90)
print("Sera gasto",v1,"litros de combustível")
print("Sera gasto",v2,"reais na viagem")

#l1= quilometros
#l2 = litros
#v1 = litros gastos
#v2 = reais

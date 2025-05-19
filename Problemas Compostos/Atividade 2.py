# passo a passo

#1- - exibir o novo preço do produto e quanto ele diminuiu

#2 - descibrir um desconto de 5% o produto

#3
#Passo1:Multiplicar o valor original do produto pela porcentagem
#Passo2:Multiplicar o novo valor por 100
#Passo3:Exibir o novo preço e quanto ele diminuiu

produto = input("digite um nome")
preco = float(input("Digite o valor"))
porcentagem = preco / 20
valor_final = preco - porcentagem
print("Com o desconto de", porcentagem, "reais,o valor final do produto será de", valor_final, "reais")

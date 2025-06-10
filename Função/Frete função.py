dis = int(input("Digite a distância: "))
peso = int(input("Digite o peso: "))
taxa = int(input("Digite a taxa fixa: "))
def calcular(dis, peso, taxa):
    return (peso * 0.5) + (dis * 0.1) + taxa

print(calcular(dis, peso, taxa), "é o valor do frete")
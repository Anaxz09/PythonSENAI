from datetime import datetime

def hora_atual(nome):
    hora = datetime.now().hour
    if hora >= 0 and hora <= 5:
        print("Boa madrugada", nome)
    elif hora > 5 and hora <= 12:
        print("Bom dia", nome)
    elif hora > 12 and hora <= 19:
        print("Boa tarde", nome)
    else:
        print("Boa noite", nome)
    

hora_atual(input("Digite seu nome "))




# O usuário possa informar o nome do aluno. 
# O sistema receba três notas e calcule a média automaticamente. 
# Com base na média, o sistema deve indicar se o aluno está "Aprovado" (média ≥ 7), "Recuperação" (entre 5 e 6.9) ou "Reprovado" (média < 5). 
# O sistema deve permitir o cadastro de vários alunos e exibir um resumo final com o nome de cada aluno e sua situação.
import inputs

alunos = []

def aluno_cadastrar():
    nome = inputs.input_str ("Digite o nome do aluno ")
    n1 = inputs.input_int ("Digite a primeira nota ")
    n2 = inputs.input_int ("Digite a segunda nota ")
    n3 = inputs.input_int ("Digite a terceira nota ")
    media = int(fazer_media(n1, n2, n3))
    situacao = veri_situ_aluno(media)
    print("")
    
    aluno1 = {
        "nome": nome,
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "media": media,
        "situacao": situacao,
    }
    
    if aluno1 in alunos:
        print("Este nome já está na lista")
   
    else:
        alunos.append(aluno1)
        print("Adicionado")
        
def fazer_media(n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    return media
    
def veri_situ_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media <= 7:
        return "Recuperação"
    elif media < 5:
        return "Reprovado"
    
def mostrar_relatorio(alunos):   
    for aluno in alunos:
        print("")
        print("Nome -",f" {aluno['nome']}")
        print("Média -",f" {aluno['media']}")
        print("Situação -",f" {aluno['situacao']}")
        print("")
        
while True:
    print("Menu")
    print("")
    print("[1] - Cadastrar o nome do aluno e a nota")
    print("[2] - Exibir as informações (O nome e as notas)")
    print("[3] - Sair")
    print("")
    escolha = inputs.input_int("Escolha uma dessas opções ")
    if escolha == 1:
        aluno_cadastrar()  
    elif escolha == 2:
        mostrar_relatorio(alunos)
    elif escolha == 3:
        print("Sair")
        break
        
        
        
    
    







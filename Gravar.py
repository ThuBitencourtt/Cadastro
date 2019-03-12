import json
import os
import json

def cadastro():
    os.system('cls' if os.name == 'nt' else 'clear')
    matricula = input("Digite sua matricula ? ")
    nome = input("\nQual é seu nome ? ")
    idade = input("\nQual sua idade ? ")
    curso = input("\nDigite o curso ? ")

    data = {}  
    data['facul'] = []  
    data['facul'].append({  
        'matricula':matricula,
        'nome': nome,
        'idade': idade,
        'curso': curso
    })
    
    with open('data.json', 'a') as outfile:  
        json.dump(data, outfile)

def excluir():
    teste = input("asdasd")
    with open('data.json', 'r') as outfile:  
        text = outfile.read()
    for teste in text[matricula]:
        del text[teste]

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n 1 - Cadastrar Aluno\n")
    print("\n 2 - Excluir Aluno \n")
    print("\n 0 - SAIR \n")
    opcao = int(input("Ecolha uma opcao: "))
    return opcao

while True:
    opcao = menu()
    if opcao == 3:
        break
    elif opcao == 1:
        cadastro()
    elif opcao == 2:
        excluir()
 

    i = 0
    while i < 1:
        teste = input("\nDeseja sair? ")
        if teste == 'sim':
            i = 1
        else: 
            cadastro()

menu()
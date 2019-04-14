#coding=utf-8

dic_cadastro = {}
dic_avaliacao = {}
dic_treino = {}


def cadastro():
    cad =[]
    name_cad = input('Digite o nome:\t').lower()
    phone = int(input('Telefone:\t'))
    idade = int(input('Idade:\t'))
    cad.append(phone)
    cad.append(idade)
    dic_cadastro[name_cad] = cad
    print(dic_cadastro)
    return()
    
def indice_massa(imc):
    if imc < 16:
	    print("Magreza grave")
    elif imc < 17:
	    print("Magreza moderada")
    elif imc < 18.5:
	    print("Magreza leve")
    elif imc < 25:
	    print("Saudável")
    elif imc < 30:
	    print("Sobrepeso")
    elif imc < 35:
        print('sei la')
    elif imc < 40:
	    print("Obesidade Grau II (severa)")
    else:
	    print("Obesidade Grau III (mórbida)")

    return()
    
def avaliacao():
    ava = []
    name_ava = input('Digite o nome do aluno:\t').lower()
    if  name_ava in dic_cadastro:
        print('aluno cadastrado!\n')
        massa = float(input('Massa corporea(kg):\t'))
        estatura =  float(input('Estatura(m):\t'))
        imc = round(float(massa/estatura**2))
        print('\nSeu IMC é: ',imc,indice_massa(imc))
        ava.append(massa)
        ava.append(estatura)
        ava.append(imc)
        dic_avaliacao[name_ava] = ava
        print(dic_avaliacao)
    else: 
        print('Aluno não cadastrado\nFavor, realizar cadastro.')
    return()

def treino():
    tre = []
    name_tre = input('Digite o nome do aluno:\t').lower()
    if  name_tre in dic_cadastro:
        print('aluno cadastrado!\n')
        num_ex = int(input('Quantidade de Exercicios para o aluno:\t'))
        for i in range(num_ex):
            exer = str(input('Exercicio:\t'))
            tre.append(exer)

    dic_treino[name_tre] = tre
    print(dic_treino)

    return()


def menu():
    opc = int(input(
    '''     Academia Skin&Bones
        Menu:
            1 - Cadastro de novos alunos
            2 - Avaliação
            3 - Treino do Aluno
    '''))
    if opc == 1:
        cadastro()
    elif opc ==2:
        avaliacao()
    elif opc == 3:
        treino()
    else:
        print('Opcão Invalida!!')
    return()


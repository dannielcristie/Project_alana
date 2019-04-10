academia = {}

def cadastro():
    cad =[]
    name_client = input('Digite o nome:\t').lower()
    phone = int(input('Telefone:\t'))
    idade = int(input('Idade:\t'))
    cad.append(phone)
    cad.append(idade)
    academia[name_client] = cad
    
    return()
    
def im_c(imc):
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
	    print("Obesidade Grau I")
    elif imc < 40:
	    print("Obesidade Grau II (severa)")
    else:
	    print("Obesidade Grau III (mórbida)")

    return()
    
    
def avaliacao():
    name_b = input('Nome do aluno:\t').lower()
    for i in academia:
        if name_b in academia:
            name_client = name_b
            ava=[]
            print('aluno cadastro')
            estatura = float(input('estatura(m):\t'))
            massa = float(input('Massa Corpórea(Kg):\t'))
            imc = massa/(estatura**2)
            print(im_c(imc))
            ava.append(estatura)
            ava.append(massa)
            ava.append(imc)
            academia[name_client] = ava
        print(academia[name_client])
            
    return()
    
    
    
	
cadastro()
avaliacao()
print(academia)
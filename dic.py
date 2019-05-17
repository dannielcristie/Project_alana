'''
dic = {}
a = input('digita ai')
b = input('digita ai')

dic['danniel'] = [a,b]

print(dic)
'''


class Dic:
    def __init__(self):
        self.chaves = []
        self.dados = []
    def inserir(self,chave,dado):
        self.chaves.append(chave)
        self.dados.append(dado)

dic = Dic()

dic.inserir('danniel',30081996)

print(dic)
















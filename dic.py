def main():
    # copie abaixo a funcao main dada anteriormente

class Dicionario:
    def __init__(self):
        self.chave = []
        self.valor = []

    def __str__(self):
        tam = len(self.chave)
        if tam == 0:
            return '{}'

        dic = '{%s:%s'%(str(self.chave[0]),str(self.valor[0]))
        for i in range(1, len(self.chave)):
            dic += ',%s:%s'%(str(self.chave[i]),str(self.valor[i]))
        dic += '}'
        return dic

    def procura(self, c):
        ''' (chave) -> int
            Recebe uma chave e devolve o indice da chave, caso
            exista e None caso contrario '''
        for i in range(len(self.chave)):
            if c == self.chave[i]:
                return i
        return None

    def insere(self, c, v):
        ''' (chave, valor) -> None
            altera o valor do par chave:valor para chave:v no
            dicionario caso a chave exista ou cria o par chave:v
            caso a chave ainda nao esteja no dicionario. '''
        # escreva abaixo o codigo para esse metodo

    def pega_valor(self, c):
        ''' (chave) -> valor
            Retorna o valor de uma chave, caso exista, ou None '''

        # escreva abaixo o codigo para esse metodo

main()

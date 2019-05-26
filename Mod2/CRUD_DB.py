from EstruturasDeDados import *
import sqlite3

con = sqlite3.connect('base.db')
cursor = con.cursor()


def db_insert_cad(name,cpf,idade,phone,email):
    return """
    INSERT  INTO clientes(name,cpf,idade,phone,email) VALUES ('{}','{}','{}','{}','{}')""".format(name,cpf,idade,phone,email)

def db_insert_ava(massa,estatura,imc,cpf):
    return """
    UPDATE clientes SET massa = '{}', estatura = '{}',imc = '{}'
    WHERE cpf = '{}' """.format(massa,estatura,imc, cpf)

def db_insert_tre(peito,biceps,triceps,cpf):
    return"""
    UPDATE clientes SET treino_peito = '{}', treino_bicpes = '{}',
    treino_triceps = '{}' WHERE cpf = '{}'""".format(peito,biceps,triceps,cpf)





#cursor.execute(db_insert_cad('Danniel',60797571337,22,981187186,'dany14012@gmail.com'))

#cursor.execute(db_insert_ava(68.5,1.80,28,60797571337))


p = Pilha()

for i in range(0,3):
    a = input('exercicio: ')
    p.empilhar(a)



cursor.execute(db_insert_tre(p,'rosca','corda',60797571337))



con.commit()
con.close()

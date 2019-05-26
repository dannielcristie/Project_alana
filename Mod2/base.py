import sqlite3

con = sqlite3.connect('base.db')

cursor = con.cursor()


cad = """
CREATE TABLE IF NOT EXISTS clientes ( id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
                        name TEXT NOT NULL,
                        cpf TEXT UNIQUE NOT NULL,
                        idade TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        email TEXT  NOT NULL,
                        imc TEXT,
                        massa TEXT ,
                        estatura TEXT,
                        treino_peito TEXT,
                        treino_bicpes TEXT ,
                        treino_triceps TEXT,
                        treino_costas TEXT ,
                        treino_pernas TEXT ,
                        treino_abd TEXT )"""



cursor.execute(cad)
con.commit()
con.close()

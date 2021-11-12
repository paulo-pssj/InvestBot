import sqlite3

class DB:
    def __init__(self, dbname="database.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)
        self.cur = self.conn.cursor()
        
    def setup(self):
        sql = """
                 CREATE TABLE IF NOT EXISTS users 
                 (
                     id INTEGER NOT NULL PRIMARY KEY UNIQUE,
                     name  TEXT,
                     lista_acoes TEXT
                 )
                 """
        self.cur.execute(sql)
        self.conn.commit()
    
    # adiciona um novo usuário (id_telegram, nome, lista_acoes NULL)
    def add_user(self, id, name):
        if self.verifica_usuario(id) == False:
            sql = """
                    INSERT INTO users (id, name) VALUES ('{}', '{}')
                """.format(id, name) 
            self.cur.execute(sql)
            self.conn.commit()
    
    # Atualiza a lista de ações do usuário
    def update_list(self, id, lista):
        sql = """
              UPDATE users SET lista_acoes = '{}' WHERE id = '{}'
              """.format(lista, id)      
        self.cur.execute(sql)
        self.conn.commit()
    
    # deleta todas informações do usuário         
    def delete_user(self, id):
        sql = """
              DELETE FROM users WHERE id = '{}'
              """.format(id)
        self.cur.execute(sql)
        self.conn.commit()
    
    # Busca lista de ações pelo id do usuário
    def busca_acoes(self, id):
        sql = """
              SELECT lista_acoes FROM users WHERE id = '{}'
              """.format(id)
        self.cur.execute(sql)
        data = self.cur.fetchone()[0]
        if data == None:
            return f'Nenhuma lista encontrada'
        return data
    
    #verifica se usuario existe e retorna True ou False
    def verifica_usuario(self, id):
        sql = """
              SELECT COUNT(1) FROM users WHERE id = '{}'
              """.format(id)
        self.cur.execute(sql)
        existe = self.cur.fetchone()[0]
        if existe == 1:
            return True
        else:
            return False



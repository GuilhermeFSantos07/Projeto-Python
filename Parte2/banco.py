import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.criarTabela()
    
    def criarTabela(self):
        c = self.conexao.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                idaluno TEXT PRIMARY KEY,
                nome TEXT,
                serie TEXT,
                turno TEXT,
                turma TEXT,
                nota1 FLOAT,
                nota2 FLOAT,
                nota3 FLOAT,
                media FLOAT,
                aprovacao TEXT
            )
        """)
        self.conexao.commit()
        c.close()
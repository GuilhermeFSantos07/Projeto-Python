import random
from banco import Banco
from datetime import datetime

class Alunos:

    def __init__(self, idaluno = "", nome = "", serie = "", turno ="", turma = "",
                 nota1 = 0.0, nota2 = 0.0, nota3 = 0.0, media = 0.0, aprovacao = ""):
        self.idaluno = idaluno
        self.nome = nome
        self.serie = serie
        self.turno = turno
        self.turma = turma
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = media
        self.aprovacao = aprovacao

    def geradorID(self):
        if self.idaluno:
            return self.idaluno
        data_atual = datetime.now()
        ano_mes = data_atual.strftime('%Y%m')
        numero_aleatorio = f"{random.randint(100000, 999999)}"
        self.idaluno = f"{ano_mes}{numero_aleatorio}"
        return self.idaluno

    def inserirAluno(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            self.geradorID()

            sql = """
                INSERT INTO alunos (idaluno, nome, serie, turno, turma, nota1, nota2, nota3, media, aprovacao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            c.execute(sql, (self.idaluno, self.nome, self.serie, self.turno, self.turma,
                            self.nota1, self.nota2, self.nota3, self.media, self.aprovacao))
            banco.conexao.commit()
            c.close()

            return "Aluno cadastrado com sucesso"
        except:
            return "Ocorreu um erro no cadastro"

    def atualizarAluno(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            sql = """
                UPDATE alunos SET nota1 = ?, nota2 = ?, nota3 = ?, media = ?, aprovacao = ?
                WHERE idaluno = ?"""
            c.execute(sql, (self.nota1, self.nota2, self.nota3, self.media, self.aprovacao, self.idaluno))
            banco.conexao.commit()
            c.close()

            return "Aluno atualizado com sucesso"
        except:
            return "Ocorreu um erro na atualização"
    
    def deletarAluno(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            sql = "DELETE FROM alunos WHERE idaluno = ?"
            c.execute(sql, (self.idaluno,))
            banco.conexao.commit()

            c.close()
            return "Aluno deletdo com sucesso"
        except:
            return "Ocorreu um erro o deletar o aluno"
    
    def procurarAluno(self, idaluno):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            sql = "SELECT * FROM alunos WHERE idaluno = ?"
            c.execute(sql, (idaluno,))
            linha = c.fetchone()
            c.close()
            if linha:
                self.idaluno, self.nome, self.serie, self.turno, self.turma, \
                self.nota1, self.nota2, self.nota3, self.media, self.aprovacao = linha
                return "Aluno encontrado"
            else:
                return "Aluno não encontrado"
        except:
            return "Ocorreu um erro ao encontrar o aluno"
        
    def procurarPorNome(self, nome):
        banco = Banco()
        try:
            c = banco.conexao.cursor()           
            sql = "SELECT * FROM alunos WHERE nome = ?"
            c.execute(sql, (nome,))
            resultados = c.fetchall()
            c.close()
            return resultados
        except:
            return "Erro ao encontrar o aluno"
        
    def listarAlunos(self, serie, turno, turma):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            sql = "SELECT nome, media, aprovacao FROM alunos WHERE serie = ? AND turno = ? AND turma = ?"
            c.execute(sql, (serie, turno, turma))
            resultados = c.fetchall()
            c.close()
            return resultados
        except:
            return "Erro ao gerar lista"
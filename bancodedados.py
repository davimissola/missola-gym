import pyodbc as bd

class BancoDeDados:

    def __init__(self):
        self.conexao = ''

    def esta_conectado(self):
        try:
            self.conexao = bd.connect('DRIVER={SQL Server};'
                                      'SERVER=seu_servidor_aqui;'
                                      'DATABASE=seu_banco_aqui;'
                                      'UID=seu_usuario_aqui;'
                                      'PWD=sua_senha_aqui;'
                                      )
            return True
        except:
            return False
        
    def cadastrar_aluno(self, cliente):
        cursor = self.conexao.cursor()

        comando = f"""
                INSERT INTO Academia.Clientes
                VALUES
                ('{cliente._nome}', {cliente._idade}, '{cliente._telefone}', '{cliente._plano}', '{cliente._status_pagamento}')
                """
        try:
            cursor.execute(comando)
            self.conexao.commit()
            return True
        except Exception as e:
            print('ERRO: ', e)
            self.conexao.rollback() # cancela qualquer atualização caso dê qualquer erro
            return False
        

    def listar_alunos(self):
        cursor = self.conexao.cursor()

        comando = "SELECT * FROM Academia.Clientes"
        cursor.execute(comando)
        alunos = cursor.fetchall()
        
        return alunos
    
    
    def buscar_aluno(self, nome):
        cursor = self.conexao.cursor()

        comando = f"""
                SELECT * FROM Academia.Clientes
                WHERE nome = '{nome}'
                """
        cursor.execute(comando)
        aluno = cursor.fetchall()

        return aluno
    

    def atualizar_stauts_pagamento(self, nome, novo_status):
        cursor = self.conexao.cursor()

        comando = f"""
                UPDATE Academia.Clientes
                SET status_pagamento = '{novo_status}'
                WHERE nome = '{nome}'
                """
        try:
            cursor.execute(comando)
            if cursor.rowcount == 0:
                cursor.rollback()
                return False
            else:
                self.conexao.commit()
                return True
        except Exception as e:
            cursor.rollback()
            return False
        

    def excluir_aluno(self, nome):
        cursor = self.conexao.cursor()

        comando = f"""
                DELETE FROM Academia.Clientes
                WHERE nome = '{nome}'
                """
        try:
            cursor.execute(comando)
            cursor.commit()
            return True
        except:
            cursor.rollback()
            return False

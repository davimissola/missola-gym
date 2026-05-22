import customtkinter as ctk
import bancodedados
import cliente

bd = bancodedados.BancoDeDados()
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title('Missola Gym')
        self.geometry('1000x700')

        # Criação de colunas e linhas
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Divisão por abas
        self.coluna_lateral = ctk.CTkFrame(self, width=200)
        self.coluna_lateral.grid(column=0, row=0, sticky='nsew')
        #-----------------------------------------------------------
        self.coluna_central = ctk.CTkTabview(self, width=400)
        self.coluna_central.grid(column=1, row=0, sticky='nsew', padx=20, pady=10)
        self.coluna_central.add('Cadastrar aluno')
        self.coluna_central.add('Listar alunos')
        self.coluna_central.add('Buscar aluno')
        self.coluna_central.add('Atualizar pagamento')
        self.coluna_central.add('Excluir aluno')

        # Chamar cada aba
        self.aba_lateral()
        self.construir_aba_cadastrar_aluno()
        self.construir_aba_listar_alunos()
        self.construir_aba_buscar_aluno()
        self.construir_aba_atualizar_pagamento()
        self.construir_aba_excluir_aluno()

    def aba_lateral(self):
        # Titulo e subtitulo principais
        titulo_principal = ctk.CTkLabel(self.coluna_lateral,
                                        text='Missola Gym',
                                        font=('Arial', 24, 'bold'),
                                        text_color="#2FA572",
                                        )
        subtitulo_principal = ctk.CTkLabel(self.coluna_lateral,
                                           text='Projeto teste',
                                           font=('Arial', 13, 'bold'),
                                           )
        titulo_principal.pack(pady=(200, 0), padx=(40))
        subtitulo_principal.pack(pady=(0, 0))

        #----------------------------------------------------------------------
        # Mudar modo claro
        self.modo_escuro = ctk.CTkSwitch(self.coluna_lateral,
                                        text='Modo escuro',
                                        font=('Arial', 13, 'bold'),
                                        command=self.mudar_modo_claro)
        self.modo_escuro.pack(pady=(400, 0))

    def construir_aba_cadastrar_aluno(self):
        aba_cadastrar_aluno = self.coluna_central.tab('Cadastrar aluno')

        # Titulo cadastrar aluno
        titulo_cadastrar_aluno = ctk.CTkLabel(aba_cadastrar_aluno,
                                              text='Cadastrar novo aluno',
                                              font=('Arial', 22, 'bold'),
                                              text_color='#2FA572',
                                              )
        titulo_cadastrar_aluno.pack(pady=(20, 0))
        #-------------------------------------------------------------------------
        # Pedir informações do aluno
        # Nome aluno
        titulo_nome = ctk.CTkLabel(aba_cadastrar_aluno,
                                   text='Nome completo: *',
                                   font=('Arial', 15, 'bold')
                                   )
        self.nome_aluno = ctk.CTkEntry(aba_cadastrar_aluno,
                                       placeholder_text='Ex: Davi Missola',
                                       width=500
                                       )
        titulo_nome.pack(pady=(10, 0))
        self.nome_aluno.pack()
        # Idade aluno
        titulo_idade = ctk.CTkLabel(aba_cadastrar_aluno,
                                    text='Idade: *',
                                    font=('Arial', 15, 'bold')
                                    )
        self.idade_aluno = ctk.CTkEntry(aba_cadastrar_aluno,
                                        placeholder_text='Insira apenas números.',
                                        width=200
                                        )
        titulo_idade.pack(pady=(10, 0))
        self.idade_aluno.pack()
        # Telefone aluno
        titulo_telefone = ctk.CTkLabel(aba_cadastrar_aluno,
                                       text='Telefone: *',
                                       font=('Arial', 15, 'bold')
                                       )
        self.telefone_aluno = ctk.CTkEntry(aba_cadastrar_aluno,
                                           placeholder_text='Insira apenas números.',
                                           width=500)
        titulo_telefone.pack(pady=(12, 0))
        self.telefone_aluno.pack()
        # Plano aluno
        titulo_plano = ctk.CTkLabel(aba_cadastrar_aluno,
                                    text='Plano: *',
                                    font=('Arial', 15, 'bold')
                                    )
        self.plano_aluno = ctk.StringVar(value='basic')
        basic = ctk.CTkRadioButton(aba_cadastrar_aluno,
                                   text='Basic',
                                   variable=self.plano_aluno,
                                   value='basic')
        gold = ctk.CTkRadioButton(aba_cadastrar_aluno,
                                  text='Gold',
                                  variable=self.plano_aluno,
                                  value='gold')
        premium = ctk.CTkRadioButton(aba_cadastrar_aluno,
                                     text='Premium',
                                     variable=self.plano_aluno,
                                     value='premium')
        titulo_plano.pack(pady=(10, 0))
        basic.pack()
        gold.pack()
        premium.pack()
        # Status Pagamento
        titulo_status = ctk.CTkLabel(aba_cadastrar_aluno,
                                     text='Status pagamento: *',
                                     font=('Arial', 15, 'bold')
                                     )
        self.status_pagamento = ctk.CTkSegmentedButton(aba_cadastrar_aluno,
                                                       values=('pago', 'pendente')
                                                       )
        self.status_pagamento.set('pendente')
        titulo_status.pack(pady=(10, 0))
        self.status_pagamento.pack()
        #---------------------------------------------------------------------------------------
        # Botão encaminhar valores
        botao = ctk.CTkButton(aba_cadastrar_aluno,
                              text='Adicionar aluno',
                              command=self.repassar_valores,
                              width=200,
                              height=40
                              )
        botao.pack(pady=(60, 0))
        # Resultado
        self.resultado = ctk.CTkLabel(aba_cadastrar_aluno,
                                      text='',
                                      font=('Arial', 15, 'bold')
                                      )
        self.resultado.pack()

    def construir_aba_listar_alunos(self):
        aba_listar_alunos = self.coluna_central.tab('Listar alunos')

        # Titulo
        titulo_listar_alunos = ctk.CTkLabel(aba_listar_alunos,
                                            text='Listar alunos',
                                            font=('Arial', 22, 'bold'),
                                            text_color='#2FA572',
                                            )
        titulo_listar_alunos.pack(pady=(20, 20))
        # Listar alunos
        # Crio uma scrolllabel para dar para rolar para baixo caso precise
        scroll_listar_alunos = ctk.CTkScrollableFrame(aba_listar_alunos,
                                                      fg_color='transparent',
                                                      width=600,
                                                      height=530,
                                                      )
        scroll_listar_alunos.pack()
        # Começa dando o peso 1 para as colunas 0 e 6 pra q fique tudo centralizado
        scroll_listar_alunos.grid_columnconfigure(0, weight=1)
        scroll_listar_alunos.grid_columnconfigure(6, weight=1)
        if bd.esta_conectado():
            lista_alunos = bd.listar_alunos()
            # Começa a criar a tabela zerando linha e coluna
            linha = 1
            for aluno in lista_alunos:
                coluna = 1
                for dado_aluno in aluno:
                    dado = ctk.CTkLabel(scroll_listar_alunos,
                                        text=f'{dado_aluno}',
                                        font=('Arial', 14, 'bold'),
                                        padx=10
                                        )
                    dado.grid(column=coluna, row=linha, sticky='w')
                    coluna += 1
                linha += 1
        else:
            pass

    def construir_aba_buscar_aluno(self):
        aba_buscar_aluno = self.coluna_central.tab('Buscar aluno')
        # Titulo
        titulo_buscar_aluno = ctk.CTkLabel(aba_buscar_aluno,
                                           text='Buscar aluno',
                                           font=('Arial', 22, 'bold'),
                                           text_color='#2FA572',
                                           )
        titulo_buscar_aluno.pack(pady=(20, 0))
        # Dados da pessoa
        titulo_nome = ctk.CTkLabel(aba_buscar_aluno,
                                   text='Nome: *',
                                   font=('Arial', 15, 'bold'),
                                   )
        self.nome_busca = ctk.CTkEntry(aba_buscar_aluno,
                                 placeholder_text='Ex: Davi Missola',
                                 width=500,
                                 )
        titulo_nome.pack(pady=(10, 0))
        self.nome_busca.pack()
        # Botao para buscar
        botao = ctk.CTkButton(aba_buscar_aluno,
                              text='Buscar aluno',
                              command=self.buscar_aluno,
                              width=200,
                              height=40,
                              )
        botao.pack(pady=(60, 0))
        #--------------------------------------------
        # Mostrar resultado
        self.dados = ctk.CTkLabel(aba_buscar_aluno,
                                  text='',
                                  font=('Arial', 18, 'bold'),
                                  )
        self.dados.pack(pady=(30, 0))

    def construir_aba_atualizar_pagamento(self):
        aba_atualizar_pagamento = self.coluna_central.tab('Atualizar pagamento')
        # Titulo atualizar pagamento
        titulo_atualizar_pagamento = ctk.CTkLabel(aba_atualizar_pagamento,
                                                  text='Atualizar pagamento de aluno',
                                                  font=('Arial', 22, 'bold'),
                                                  text_color='#2FA572',
                                                  )
        titulo_atualizar_pagamento.pack(pady=(20, 0))
        # Pedir informações do aluno
        # Nome aluno
        titulo_nome = ctk.CTkLabel(aba_atualizar_pagamento,
                                   text='Nome completo: *',
                                   font=('Arial', 15, 'bold')
                                   )
        self.nome_pagamento = ctk.CTkEntry(aba_atualizar_pagamento,
                                       placeholder_text='Ex: Davi Missola',
                                       width=500
                                       )
        titulo_nome.pack(pady=(10, 0))
        self.nome_pagamento.pack()
        # Status Pagamento
        titulo_status = ctk.CTkLabel(aba_atualizar_pagamento,
                                     text='Novo status pagamento: *',
                                     font=('Arial', 15, 'bold')
                                     )
        self.status_pagamento_att = ctk.CTkSegmentedButton(aba_atualizar_pagamento,
                                                       values=('pago', 'pendente')
                                                       )
        self.status_pagamento_att.set('pendente')
        titulo_status.pack(pady=(10, 0))
        self.status_pagamento_att.pack()
        # Botao
        botao = ctk.CTkButton(aba_atualizar_pagamento,
                              text='Atualizar pagamento',
                              command=self.atualizar_status_pagamento,
                              width=200,
                              height=40
                              )
        botao.pack(pady=(60, 0))
        #------------------------------------------------------
        # Resultado
        self.resultado_pagamento = ctk.CTkLabel(aba_atualizar_pagamento,
                                 text='',
                                 font=('Arial', 15, 'bold')
                                 )
        self.resultado_pagamento.pack()

    def construir_aba_excluir_aluno(self):
        aba_excluir_aluno = self.coluna_central.tab('Excluir aluno')
        # Titulo atualizar pagamento
        titulo_excluir_aluno = ctk.CTkLabel(aba_excluir_aluno,
                                            text='Excluir aluno',
                                            font=('Arial', 22, 'bold'),
                                            text_color='#2FA572',
                                            )
        titulo_excluir_aluno.pack(pady=(20, 0))
        # Pedir informações do aluno
        # Nome aluno
        titulo_nome = ctk.CTkLabel(aba_excluir_aluno,
                                   text='Nome completo: *',
                                   font=('Arial', 15, 'bold')
                                   )
        self.nome_exclusao = ctk.CTkEntry(aba_excluir_aluno,
                                        placeholder_text='Ex: Davi Missola',
                                        width=500
                                        )
        titulo_nome.pack(pady=(10, 0))
        self.nome_exclusao.pack()
        # Botao
        botao = ctk.CTkButton(aba_excluir_aluno,
                              text='Excluir aluno',
                              command=self.excluir_aluno,
                              width=200,
                              height=40
                              )
        botao.pack(pady=(60, 0))
        #------------------------------------------------------
        # Resultado
        self.resultado_exclusao = ctk.CTkLabel(aba_excluir_aluno,
                                            text='',
                                            font=('Arial', 15, 'bold')
                                            )
        self.resultado_exclusao.pack()
    
    def mudar_modo_claro(self):
        if self.modo_escuro.get() == 0:
            ctk.set_appearance_mode('Light')
        else:
            ctk.set_appearance_mode('Dark')

    def repassar_valores(self):
        try:
            novo_aluno = cliente.Cliente()
            novo_aluno.atribuir_dados(self.nome_aluno.get(), int(self.idade_aluno.get()), int(self.telefone_aluno.get()), self.plano_aluno.get(), self.status_pagamento.get())

            if bd.esta_conectado():
                if bd.cadastrar_aluno(novo_aluno):
                    self.resultado.configure(text='Aluno cadastrado.')
                else:
                    self.resultado.configure(text='Não foi possível cadastrar o aluno.')
            else:
                self.resultado.configure(text='Não foi possível acessar o banco de dados.')
            # Apaga as informações que o usuario digitou
            self.nome_aluno.delete(0, 'end')
            self.idade_aluno.delete(0, 'end')
            self.telefone_aluno.delete(0, 'end')
            self.plano_aluno.set('basic')
            self.status_pagamento.set('pendente')
        except Exception as e:
            self.resultado.configure(text=f'{e}')

        # Depois de 5 segundos, apaga a mensagem deixada se deu ou não certo
        self.after(5000, lambda: self.resultado.configure(text=''))

    def buscar_aluno(self):
        try:
            if bd.esta_conectado():
                aluno = bd.buscar_aluno(self.nome_busca.get())
                if aluno != []:
                    self.dados.configure(text=f"""
Id : {aluno[0][0]}
Nome : {aluno[0][1]}
Idade : {aluno[0][2]}
Telefone : {aluno[0][3]}
Plano : {aluno[0][4]}
Status de Pagamento : {aluno[0][5]}
"""
)
                    self.nome_busca.delete(0, 'end')
                else:
                    self.dados.configure(text='Aluno não encontrado.')
                    self.nome_busca.delete(0, 'end')
                    self.after(5000, lambda: self.dados.configure(text=''))
            else:
                self.dados.configure(text='Não foi possível conectar ao banco de dados.')
                self.nome_busca.delete(0, 'end')
                self.after(5000, lambda: self.dados.configure(text=''))
        except Exception as e:
            self.dados.configure(text=f'Ocorreu um erro. {e}')

    def atualizar_status_pagamento(self):
        if bd.esta_conectado():
            if bd.atualizar_stauts_pagamento(self.nome_pagamento.get(), self.status_pagamento_att.get()):
                self.resultado_pagamento.configure(text='Status de pagamento atualizado.')
            else:
                self.resultado_pagamento.configure(text='Não foi possível atualizar status de pagamento.')
        else:
            self.resultado_pagamento.configure(text='Não foi possível conectar ao banco de dados.')
        self.nome_pagamento.delete(0, 'end')
        self.after(5000, lambda: self.resultado_pagamento.configure(text=''))

    def excluir_aluno(self):
        if bd.esta_conectado():
            if bd.excluir_aluno(self.nome_exclusao.get()):
                self.resultado_exclusao.configure(text='Aluno excluído')
            else:
                self.resultado_exclusao.configure(text='Não foi possível excluir aluno. Verifique as informações passadas.')
        else:
            self.resultado_exclusao.configure(text='Não foi possível conectar ao banco de dados.')
        self.nome_exclusao.delete(0, 'end')
        self.after(5000, lambda: self.resultado_exclusao.configure(text=''))
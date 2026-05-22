from colorama import init, Fore
init(autoreset=True)

class Cliente:

    def __init__(self):
        self._nome = ''
        self._idade = 0
        self._telefone = ''
        self._plano = '' 
        self._status_pagamento = ''

    def atribuir_dados(self, nome, idade, telefone, plano, status_pagamento):
        self.nome = nome 
        self.idade = idade 
        self.telefone = telefone 
        self.plano = plano 
        self.status_pagamento = status_pagamento 

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if valor == '':
            raise ValueError('ERRO! O nome não pode ser nulo.')
        self._nome = valor

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int):
            raise ValueError('ERRO! Digite apenas números na idade.')
        if valor < 0:
            raise ValueError('ERRO! Idade precisa ser maior que 0.')
        self._idade = valor
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor):
        if valor == '':
            raise ValueError('ERRO! O telefone não pode ser nulo.')
        if isinstance(valor, int):
            self._telefone = valor
        else:
            raise ValueError('ERRO! Digite apenas números no telefone.')

    @property
    def plano(self):
        return self._plano
    
    @plano.setter
    def plano(self, valor):
        if valor not in ('basic', 'gold', 'premium'):
            raise ValueError('ERRO! Este plano não existe. Use "basic", "gold" ou "premium".')
        self._plano = valor

    @property
    def status_pagamento(self):
        return self._status_pagamento
    
    @status_pagamento.setter
    def status_pagamento(self, valor):
        if valor not in ('pago', 'pendente'):
            raise ValueError('ERRO! Este status de pagamento não existe. Use "pago" ou "pendente".')
        self._status_pagamento = valor
    
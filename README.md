# Missola Gym - Desktop

Sistema Desktop para gerenciamento e controle de alunos de uma academia. Desenvolvido em Python utilizando a biblioteca **CustomTkinter** para a interface gráfica e integrado a um banco de dados relacional **SQL Server** via `pyodbc`.

---

## Demonstração Visual

### Interface Principal & Cadastro (Tema Dark)
![Cadastro de Alunos](<img width="1001" height="723" alt="temadark" src="https://github.com/user-attachments/assets/1a3d899e-a403-484c-8a4d-1bca855b332a" />)

### Alternância para Tema Light & Listagem
![Modo Claro](<img width="999" height="730" alt="temalight" src="https://github.com/user-attachments/assets/149d8b2e-2f89-4298-be33-7db79e35b2bd" />)

---

## Funcionalidades do Sistema (CRUD Completo)

* **Cadastrar Aluno:** Captura os dados da interface e valida campos (Nome, Idade, Telefone) com regras de negócios específicas usando `@property` (Getters/Setters).
* **Listar Alunos:** Exibe de forma estruturada todos os dados vindos do banco dentro de um componente de rolagem (`CTkScrollableFrame`).
* **Buscar Aluno:** Consulta rápida na base de dados trazendo todas as informações do aluno pelo nome informado.
* **Atualizar Pagamento:** Altera o status financeiro do aluno diretamente no banco (`pago` ou `pendente`).
* **Excluir Aluno:** Remove por completo o registro do aluno da base de dados SQL Server.
* **Modo Escuro Dinâmico:** Um Switch que altera o tema do app e recria os componentes na tela em tempo real para manter as cores dos textos legíveis.

---

## Tecnologias Utilizadas

* **Linguagem:** Python
* **Interface Gráfica (GUI):** CustomTkinter
* **Banco de Dados:** SQL Server
* **Driver de Banco:** `pyodbc`

---

## Estrutura do Código

O projeto foi estruturado utilizando conceitos de Programação Orientada a Objetos (POO), separando as responsabilidades em arquivos:

* `main.py`: Inicializa e roda o loop principal do aplicativo.
* `interface.py` ou `maininterface.py`: Gerencia toda a parte visual, o grid de abas e os eventos dos botões.
* `cliente.py`: Contém a classe `Cliente` com o encapsulamento, validações de erro e regras de negócio.
* `bancodedados.py`: Cuida de toda a comunicação com o SQL Server (conexão, comandos SQL, commits e rollbacks).

---

## Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone [https://github.com/davimissola/missola-gym.git](https://github.com/davimissola/missola-gym.git)
cd missola-gym

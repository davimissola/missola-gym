### Sistema de uma Academia - Desktop

Sistema Desktop para gerenciamento e controle de alunos de uma academia. Desenvolvido em Python utilizando a biblioteca **CustomTkinter** para a interface gráfica e integrado a um banco de dados relacional **SQL Server** via `pyodbc`.

---

Demonstração Visual

Interface Principal & Cadastro (Tema Dark)
<img width="1001" height="723" alt="temadark" src="https://github.com/user-attachments/assets/d73e76b8-7eb7-4ff7-b659-9fc5cfe62a59" />

Alternância para Tema Light & Listagem
<img width="999" height="730" alt="temalight" src="https://github.com/user-attachments/assets/e0627fdf-ee28-4f4a-bb70-df9c11f4ba48" />


---

Funcionalidades do Sistema (CRUD Completo)

* **Cadastrar Aluno:** Captura os dados da interface e valida campos (Nome, Idade, Telefone) com regras de negócios específicas usando `@property` (Getters/Setters).
* **Listar Alunos:** Exibe de forma estruturada todos os dados vindos do banco dentro de um componente de rolagem (`CTkScrollableFrame`).
* **Buscar Aluno:** Consulta rápida na base de dados trazendo todas as informações do aluno pelo nome informado.
* **Atualizar Pagamento:** Altera o status financeiro do aluno diretamente no banco (`pago` ou `pendente`).
* **Excluir Aluno:** Remove por completo o registro do aluno da base de dados SQL Server.
* **Modo Escuro Dinâmico:** Um Switch que altera o tema do app e recria os componentes na tela em tempo real para manter as cores dos textos legíveis.

---

Tecnologias Utilizadas

* **Linguagem:** Python
* **Interface Gráfica (GUI):** CustomTkinter
* **Banco de Dados:** SQL Server
* **Driver de Banco:** `pyodbc`

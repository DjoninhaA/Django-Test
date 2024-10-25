
# API de Gerenciamento de Funcionários.

Este projeto é uma API desenvolvida em Django para gerenciar funcionários. A API permite realizar operações CRUD (Create, Read, Update, Delete) para a entidade Funcionário, sem o uso do Django REST Framework.

## Como Rodar o Projeto Localmente

### Pré-requisitos

- Python 3.x
- Django 3.x
- SQLite (ou outro banco de dados de sua preferência)

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd Django-Test
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

6. Acesse `http://localhost:8000/api` para testar a API.

## Endpoints

### Funcionários

1. **Listar Funcionários**
   - **URL**: `/funcionarios/`
   - **Método**: `GET`
   - **Descrição**: Retorna a lista de todos os funcionários cadastrados.
   - **Exemplo de Requisição**:

     ```bash
     http://localhost:8000/api/funcionarios/
     ```

2. **Criar Funcionário**
   - **URL**: `/funcionarios/`
   - **Método**: `POST`
   - **Descrição**: Cria um novo funcionário.
     - **Exemplo de Requisição**:

     ```bash
     http://localhost:8000/api/funcionarios/
     ```
     
   - **Body**:
     ```json
     {
      "nome": "Pedro Silva",
      "email": "pedro.silva@email.com",
      "departamento": "Tester"
     }

     ```

3. **Detalhar Funcionário**
   - **URL**: `/funcionario/<id>`
   - **Método**: `GET`
   - **Descrição**: Retorna os detalhes de um funcionário específico pelo ID.
   - **Exemplo de Requisição**:
     ```bash
      http://localhost:8000/api/funcionario/update/1
     ```

4. **Atualizar Funcionário**
   - **URL**: `/funcionario/<id>`
   - **Método**: `PUT`
   - **Descrição**: Atualiza os dados de um funcionário.
   - **Exemplo de Requisição**:
     ```bash
      http://localhost:8000/api/funcionario/update/1
     ```
      - **Body**:
       ```json
       {
        "nome": "Pedro Silva",
        "email": "pedro.silva@email.com",
        "departamento": "developer"
       }
  
       ```

5. **Excluir Funcionário**
   - **URL**: `/funcionario/delete/<id>`
   - **Método**: `DELETE`
   - **Descrição**: Remove um funcionário específico.
   - **Exemplo de Requisição**:
     ```bash
       http://localhost:8000/api/funcionario/delete/1
     ```

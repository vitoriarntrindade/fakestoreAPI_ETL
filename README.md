# FastAPI ETL - FakeStore API + MySQL + PyTest

![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-blue?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=flat-square&logo=mysql)
![TestContainers](https://img.shields.io/badge/TestContainers-MySQL-green?style=flat-square&logo=docker)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple?style=flat-square&logo=pandas)

📌 **Um sistema ETL (Extract, Transform, Load) baseado no FastAPI para consumir produtos da FakeStore API, armazená-los no MySQL e gerar relatórios estratégicos em Excel.**

---

## 📌 **Arquitetura do Projeto**

Este projeto segue o padrão **Adapter**. A API FakeStore é consumida, os dados são transformados (com timestamp e ajustes de formato) e armazenados no banco MySQL. A aplicação expõe endpoints para recuperação dos dados processados.

📌 **Fluxo do ETL:**
1️⃣ **Extract** - Baixa os produtos da API FakeStore.

2️⃣ **Transform** - Adiciona timestamp e adapta os dados.

3️⃣ **Load** - Insere no banco MySQL.

4️⃣ **API** - Disponibiliza endpoints para consumo.

5️⃣ **Relatório** - Gera um arquivo Excel com estatísticas e gráficos.

![image](https://github.com/user-attachments/assets/04dd5e30-c3bc-4824-bc61-96c4c2928612)


---

## 🛠 **Tecnologias Utilizadas**

🔹 **Linguagem**: Python 3.12  
🔹 **Framework**: FastAPI  
🔹 **Banco de Dados**: MySQL  
🔹 **ORM**: SQLAlchemy + Alembic  
🔹 **Testes**: Pytest + TestContainers  
🔹 **Processamento de Dados**: Pandas  
🔹 **Automação de Testes**: Playwright  
🔹 **Relatórios Excel**: OpenPyXL  

---

## ⚡ **Instalação e Execução**

### 🔹 **1. Clone o Repositório**
```bash
git clone https://github.com/seu-usuario/fakestoreAPI_ETL.git
cd fakestoreAPI_ETL
```

### 🔹 **2. Configure o Ambiente Virtual**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate    # Windows
```

### 🔹 **3. Instale as Dependências**
```bash
pip install -r requirements.txt
```

### 🔹 **4. Configure o Banco de Dados**
Se estiver usando MySQL local, crie o banco:
```sql
CREATE DATABASE fakestore_db;
```
Caso use **TestContainers**, ele será criado automaticamente nos testes.

### 🔹 **6. Inicie a API**
```bash
uvicorn app.main:app --reload
```
✅ A API estará disponível em **http://127.0.0.1:8000/docs**

---

## 🔍 **Endpoints Disponíveis**
| Método  | Endpoint        | Descrição |
|---------|---------------|------------|
| `POST`  | `/api/etl/start` | Inicia o processo ETL |
| `GET`   | `/api/products` | Retorna todos os produtos processados |
| `GET`   | `/api/report` | Gera e baixa o relatório Excel |

---

## ✅ **Rodando os Testes**

📌 **Testes Unitários e de API** (Banco de dados isolado com TestContainers)
```bash
pytest -v
```
📌 **Testes de Upload Automático com Playwright** (em desenvolvimento)
```bash
pytest app/tests/test_upload.py -v
```

---

## 📊 **Gerando Relatórios**
A API gera um **relatório Excel com estatísticas e gráficos**:
```bash
curl -X GET http://127.0.0.1:8000/api/relatorio -o relatorio.xlsx
```

Exemplo do relatório gerado:
📊 **Tabela de produtos formatada**

📈 **Gráfico comparativo de preços**

🔴 **Destaque para produtos acima de R$100**

🟢 **Produtos abaixo de R$100 destacados em verde**


## ⚡ **Contato**

🔹 **LinkedIn**: [linkedin.com/in/seu-perfil](https://linkedin.com/in/vitoria-raymara)  




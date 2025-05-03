# Projeto ANAC — Nova Tabela com Psycopg2

Este projeto é uma continuação do projeto original de importação de dados da ANAC.  
Seu foco principal está na criação de uma **nova tabela** no banco de dados PostgreSQL e na adaptação do script Python para integrá-la corretamente.

---

## 🔧 Funcionalidades

- Leitura de arquivo `.json` com dados da ANAC.
- Seleção e limpeza das colunas relevantes.
- Criação e utilização de nova estrutura de tabela no banco.
- Inserção de dados linha a linha na nova tabela.
- Execução de comandos SQL auxiliares no PostgreSQL.

---

## 🧰 Tecnologias Utilizadas

- **Python** — para orquestrar o processo de ETL.
- **Pandas** — para tratamento dos dados.
- **psycopg2** — para conexão e inserção de dados no PostgreSQL.
- **PostgreSQL** — banco de dados relacional.

---

## 🗂️ Estrutura da Tabela `anac_mapeamento`

A nova tabela foi criada com a seguinte estrutura:

```sql
CREATE TABLE IF NOT EXISTS anac_mapeamento (
    ID INT,
    Classificacao_da_Ocorrencia VARCHAR(50),
    Dt_Ocorrencia DATE,
    Municipio VARCHAR(50),
    UF VARCHAR(30),
    Regiao VARCHAR(30),
    Fabricante VARCHAR(100),
    Modelo VARCHAR(30)
);
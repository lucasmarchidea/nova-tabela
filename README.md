Projeto ANAC — Nova Tabela
Este projeto é uma extensão do projeto anterior de importação de dados da ANAC para o banco de dados PostgreSQL. A principal modificação foi a criação de uma nova tabela no banco e a adaptação do código para trabalhar com ela.

O que foi feito: Criada uma nova tabela no banco de dados PostgreSQL.

Adaptado o script Python para: 
Conectar ao banco de dados.
Inserir os dados na nova tabela criada.

Utilizado o código base do projeto anterior, com ajustes apenas na estrutura de destino (tabela e colunas).

Sobre os códigos usados no banco de dados:

   CREATE TABLE IF NOT EXISTS anac_mapeamento (
        ID int,
        Classificacao_da_Ocorrencia VARCHAR(50),
        Dt_Ocorrencia DATE,
        Municipio VARCHAR(50),
        UF VARCHAR(30),
        Regiao VARCHAR(30),
        Fabricante VARCHAR(100)
    )
	
    	SELECT column_name
FROM information_schema.columns
WHERE table_name = 'anac_mapeamento';

ALTER TABLE anac_mapeamento
ADD COLUMN nome_da_nova_coluna tipo_de_dados;

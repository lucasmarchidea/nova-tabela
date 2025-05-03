
import pandas as pd
import psycopg2


caminho_do_arquivo = r"C:\Users\Luq\Downloads\Curso eng dados\Arquivos\01. Postgree\Origem de dados\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')


colunas = ["Numero_da_Ocorrencia", "Classificacao_da_Ocorrência", "Data_da_Ocorrencia","Municipio","UF","Regiao","Nome_do_Fabricante", "Modelo"]
df = df[colunas]
df.rename( columns={  'Classificacao_da_Ocorrência' : 'Classificacao_da_Ocorrencia'  } ,inplace=True )


# Parâmetros de conexão
dbname   = 'python'
user     = 'postgres'
password = '123456'
host     = 'localhost'
port     = '5432' 

conexao = psycopg2.connect(dbname=dbname,user=user,password=password,host=host,port=port)
cursor = conexao.cursor()

#Delete base antes da carga
cursor.execute("delete from public.anac_mapeamento")

#Carga de Dados
for indice,coluna_df in df.iterrows():
    cursor.execute( """   insert into anac_mapeamento (     
                ID, 
                Classificacao_da_Ocorrencia, 
                Dt_Ocorrencia, 
                Municipio, 
                UF, 
                Regiao, 
                Fabricante,
                Modelo                
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) 
                
            """ ,(
                coluna_df["Numero_da_Ocorrencia"],
                coluna_df["Classificacao_da_Ocorrencia"],
                coluna_df["Data_da_Ocorrencia"],
                coluna_df["Municipio"],
                coluna_df["UF"],
                coluna_df["Regiao"],
                coluna_df["Nome_do_Fabricante"],
                coluna_df["Modelo"]    
            )                
            )

conexao.commit() 
cursor.close()
conexao.close()

# Códigos usados no banco de dados:

''' Sobre os códigos usados no banco de dados:

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
ADD COLUMN nome_da_nova_coluna tipo_de_dados; '''

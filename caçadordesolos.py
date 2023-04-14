
import requests
import mysql.connector
from bs4 import BeautifulSoup

# faz a requisição HTTP
url = "https://ainfo.cnptia.embrapa.br/digital/bitstream/item/122505/1/Doc-169-Perguntas-e-Respostas.pdf"
response = requests.get(url)
print(response)

# analisa o conteúdo HTML da resposta
soup = BeautifulSoup(response.content, 'html.parser')

# encontra os elementos relevantes na página
dados = soup.find_all('div', class_='dados')

# estabelece uma conexão com o banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="seu_banco_de_dados"
)

# insere os dados no banco de dados
cursor = mydb.cursor()
for dado in dados:
  sql = "INSERT INTO tabela_dados (valor) VALUES (%s)"
  val = (dado.text,)
  cursor.execute(sql, val)

mydb.commit()
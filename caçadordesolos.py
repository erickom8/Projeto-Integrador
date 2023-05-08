import mysql.connector

dados = 'lerpdf.py'

# estabelece uma conexão com o banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Erick_Cirico2208",
  database="PI"
)

# insere os dados no banco de dados
cursor = mydb.cursor()
for dado in dados:
  sql = "INSERT INTO ____ (____) VALUES (___)"
  val = (dado.text,)
  cursor.execute(sql, val)

mydb.commit()
from postgreService import postgreService

banco = postgreService('localhost', 'mercados', 'postgres', 'each2019')

response = banco.query('SELECT * FROM endereco')
print(response)
banco.close()
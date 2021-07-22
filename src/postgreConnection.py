import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(host='localhost', database='mercados', user='postgres', password='each2019')
cursor = connection.cursor(cursor_factory=RealDictCursor)


def mutation(sql):
    try:
        cursor.execute(sql)
        connection.commit()
        print("Mutation realizada com sucesso")
        return
    except Exception as e:
        raise Exception("Erro na mutation: " + str(e))


def query(sql):
    try:
        cursor.execute(sql)
        response = cursor.fetchall()
        print("Query realizada com sucesso")
        return response
    except Exception as e:
        raise Exception("Erro na query: " + str(e))

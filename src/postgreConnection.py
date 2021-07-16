import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(host = 'localhost', database = 'mercados', user = 'postgres', password = 'each2019')
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
    



# class postgreConnection(object):

#     connection = None

#     def __init__(self):
#         self.connection = psycopg2.connect(host = 'localhost', database = 'mercados', user = 'postgres', password = 'each2019')

#     def mutation(self, sql):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(sql)
#             cursor.close()
#             self.connection.commit()
#         except:
#             print("Deu ruim na mutation")
#             return False        
#         print("Deu bom na mutation")
#         return True
    
#     def query(self, sql):
#         response=None
#         try:
#             cursor = self.connection.cursor(cursor_factory=RealDictCursor)
#             cursor.execute(sql)
#             response = cursor.fetchall()
#         except:
#             print("Deu ruim na query")
#             return None
#         print("Deu bom na query")
#         return response
    
#     def close(self):
#         self.connection.close()

#         (host='localhost', database='mercados', user='postgres', password='each2019')
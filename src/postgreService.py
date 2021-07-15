import psycopg2

class postgreService(object):
    connection=None
    def __init__(self, mhost, db, usr, pwd):
        self.connection = psycopg2.connect(host=mhost, database=db, user=usr, password=pwd)

    def mutation(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            cursor.close()
            self.connection.commit()
        except:
            print("Deu ruim na mutation")
            return False        
        print("Deu bom na mutation")
        return True
    
    def query(self, sql):
        response=None
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            response = cursor.fetchall()
        except:
            print("Deu ruim na query")
            return None
        print("Deu bom na query")
        return response
    
    def close(self):
        self.connection.close()

        #(host='localhost', database='mercados', user='postgres', password='each2019')
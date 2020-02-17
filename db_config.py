import psycopg2


class Database:

    # connect to db
    @staticmethod
    def openConnection():

        connection = psycopg2.connect(
            host='localhost',
            port=5432,
            database='notes_manager',
            user='postgres',
            password='123456'
        )

        if connection:
            return connection

        return False

    # close connection to db
    def closeConnection(connection, cursor):
        if connection:
            cursor.close()
            connection.close()

import db_config

db = db_config.Database

connection = db.openConnection()
cursor = connection.cursor()


class Note:

    def showNotes():

        try:
            sql = " SELECT * FROM note ORDER BY create_date DESC "
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            db.closeConnection(connection, cursor)

from ..db import DB as database
import psycopg2

db = database()

def authorize(email, password):
    try:
        Cursor = db.Cursor()
        query = """ SELECT UID_USER, NAMA, EMAIL, STATUS, TGL_JOIN, LEVEL FROM MD_USER WHERE EMAIL = %s AND PASSWORD = %s; """
        values = (email, password)

        Cursor.execute(query, values)
        count = Cursor.rowcount
        data = Cursor.fetchall()
        db.connect.commit()
        if count > 0:
            return data[0]
        else:
            return data
    except (Exception, psycopg2.Error) as error:
        print("Failed to authenticate user : ", error)
    finally:
        # closing database connection.
        if db.connect is not None:
            Cursor.close()
            db.connect.close()
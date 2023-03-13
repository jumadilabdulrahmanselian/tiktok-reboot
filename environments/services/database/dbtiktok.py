from ..db import DB as database
import psycopg2

db = database()

def getAllPath():
    try:
        Cursor = db.Cursor()
        query = """ SELECT * FROM MD_PATH """

        Cursor.execute(query)
        data = Cursor.fetchall()
        db.connect.commit()
        return data
    except (Exception, psycopg2.Error) as error:
        print("Failed to Get All Path : ", error)
    finally:
        # closing database connection.
        if db.connect is not None:
            Cursor.close()
            db.connect.close()

def getPathByOS(operatingSystem):
    try:
        Cursor = db.Cursor()
        query = """ SELECT * FROM MD_PATH WHERE OS = %s """
        values = (operatingSystem, )
        Cursor.execute(query, values)
        data = Cursor.fetchall()
        db.connect.commit()
        return data
    except (Exception, psycopg2.Error) as error:
        print("Failed to Get All Path : ", error)
    finally:
        # closing database connection.
        if db.connect is not None:
            Cursor.close()
            db.connect.close()

def getUsernameByUser(idUser, roleUser):
    try:
        Cursor = db.Cursor()
        if roleUser == 'ADMIN':
            query = """ SELECT *, (SELECT COUNT(*) FROM MD_VIDEOS WHERE USERNAME = A.USERNAME) AS TOTAL_VIDEO FROM MD_USERNAME A ORDER BY TGL_INSERT DESC """
            Cursor.execute(query)
        else:
            query = """ SELECT B.USERNAME, B.STATUS, B.FOTO_PROFIL, B.SIGNATURE, B.TGL_INSERT, B.TGL_UPDATE, (SELECT COUNT(*) FROM MD_VIDEOS WHERE USERNAME = B.USERNAME) AS TOTAL_VIDEO FROM D_RELATION_USER A JOIN MD_USERNAME B ON A.USERNAME = B.USERNAME WHERE UID_USER = %s  ORDER BY B.TGL_INSERT DESC """
            values = (idUser, )
            Cursor.execute(query, values)
        
        count = Cursor.rowcount
        db.connect.commit()
        data = Cursor.fetchall()
        if count > 0:
            dd = db.convertToDict(Cursor, data)
            return dd
            # return data
        else:
            return data
    except (Exception, psycopg2.Error) as error:
        print("Failed to Get Username : ", error)
    finally:
        # closing database connection.
        if db.connect is not None:
            Cursor.close()
            db.connect.close()

def getVideosByUsername(username):
    try:
        Cursor = db.Cursor()
        query = """ SELECT * FROM MD_VIDEOS WHERE USERNAME =  %s ORDER BY ID_VIDEO DESC """
        values = (username, )
        Cursor.execute(query, values)
        
        count = Cursor.rowcount
        db.connect.commit()
        data = Cursor.fetchall()
        if count > 0:
            dd = db.convertToDict(Cursor, data)
            return dd
            # return data
        else:
            return data
    except (Exception, psycopg2.Error) as error:
        print("Failed to Get Username : ", error)
    finally:
        # closing database connection.
        if db.connect is not None:
            Cursor.close()
            db.connect.close()

def isUsernameExist(username):
    try:
        Cursor = db.Cursor()
        query = """ SELECT * FROM MD_USERNAME WHERE USERNAME = %s """
        values = (username, )
        Cursor.execute(query, values)
        count = Cursor.rowcount
        db.connect.commit()
        
        if count > 0:
            return True
        else:
            Cursor2 = db.Cursor()
            query2 = """ SELECT * FROM MD_HISTORY_USERNAME WHERE OLD_USERNAME = %s """
            values2 = (username, )
            Cursor2.execute(query2, values2)
            count2 = Cursor2.rowcount        
            db.connect.commit()

            if count2 > 0:
                return True
            else:
                return False
    except (Exception, psycopg2.Error) as error:
        print("Failed to Get Username : ", error)
    finally:
        # closing database connection.
        if db.connect is not None:
            Cursor.close()
            db.connect.close()

def getFromHistory(username, old_username=None):
    try:
        Cursor = db.Cursor()
        query = """ SELECT * FROM MD_HISTORY_USERNAME WHERE NEW_USERNAME = %s ORDER BY TGL_INSERT DESC """
        values = (username, )
        Cursor.execute(query, values)
        data = Cursor.fetchone()
        db.connect.commit()
        if data is None:
            return old_username
        else:
            return getFromHistory(data[2], data)
    except (Exception, psycopg2.Error) as error:
        print("Failed to Get Username : ", error)
    finally:
        # closing database connection.
        if db.connect is not None:
            Cursor.close()
            db.connect.close()

def saveUsername(username, status, foto, nickname, signature):
    try:
        Cursor = db.Cursor()
        # print(foto)
        query = """ INSERT INTO MD_USERNAME(USERNAME, STATUS, FOTO_PROFIL, NICKNAME, SIGNATURE, TGL_INSERT) VALUES (%s, %s, %s, %s, %s, 'now()') """
        values = (username, status, foto, nickname, signature)
        Cursor.execute(query, values)
        db.connect.commit()
        return True
    except (Exception, psycopg2.Error) as error:
        print("Failed to Save Username : ", error)
        return False
    finally:
        # closing database connection.
        if db.connect is not None:
            Cursor.close()
            db.connect.close()

def saveVideo(id_video, username, link):
    try:
        Cursor = db.Cursor()
        qSelect = """ SELECT * FROM MD_VIDEOS WHERE ID_VIDEO = %s """
        vSelect = (id_video,)
        Cursor.execute(qSelect, vSelect)
        count = Cursor.rowcount
        if count == 0:
            query = """ INSERT INTO MD_VIDEOS(ID_VIDEO, USERNAME, LINK, TGL_INSERT) VALUES (%s, %s, %s, 'now()') """
            values = (id_video, username, link)
            Cursor.execute(query, values)
        db.connect.commit()
        return True
    except (Exception, psycopg2.Error) as error:
        print("Failed to Save Video : ", error)
        return False
    finally:
        # closing database connection.
        if db.connect is not None:
            Cursor.close()
            db.connect.close()
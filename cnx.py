import pymysql
def coneccion():
    conn = pymysql.connect(
        db='trabajadores',
        user='root',
        passwd='',
        host='localhost')
    c = conn.cursor()
    return c,conn

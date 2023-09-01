from multiprocessing import connection
import mysql.connector


def conexion():
    connection = mysql.connector.connect(host='localhost',

                                             database='reciclaje1',
                                             user='root',
                                             password='')

    print("funcion conexion")        
    return connection                                    
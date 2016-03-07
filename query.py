#!/usr/bin/env python3
# -*-coding:utf-8-*-

# http://www.mysqltutorial.org/python-mysql-query/

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def getData():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(("""
                        select
                            table.row
                        from
                            table
                       """))

        rows = cursor.fetchall()

        return rows

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

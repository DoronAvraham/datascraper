import psycopg2
import sqlite3

__DB_NAME = "my_cocktails_bar.db"


def handler_postgresql():
    return psycopg2.connect(database = __DB_NAME,
                        user = "doron",
                        host= 'localhost',
                        port = 5432)

def handler_sqlite():
    return sqlite3.connect(__DB_NAME)
